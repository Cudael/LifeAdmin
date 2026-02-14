"""
Password management endpoints for authentication
"""
from fastapi import APIRouter, HTTPException, Depends, Request
from sqlmodel import Session, select
from datetime import datetime, timedelta
import secrets
import sqlite3
import os
import logging

from database import get_session
from models.user import User
from utils.auth import (
    hash_password,
    verify_password,
    get_current_user
)
from slowapi import Limiter
from slowapi.util import get_remote_address

from ._schemas import (
    ForgotPasswordRequest,
    ResetPasswordRequest,
    VerifyTokenRequest
)
from ._validation import validate_password
from ._email import send_password_reset_email

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)
logger = logging.getLogger(__name__)


# -----------------------------
# CHANGE PASSWORD
# -----------------------------

@router.post("/change-password")
@limiter.limit("5/hour")  # ✅ Prevent brute force
async def change_password(
    request: Request,
    password_data: dict,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Change user password"""
    
    current_password = password_data.get("current_password")
    new_password = password_data.get("new_password")
    
    if not current_password or not new_password:
        raise HTTPException(status_code=400, detail="Current and new password required")
    
    # Verify current password
    if not user.password_hash or not verify_password(current_password, user.password_hash):
        logger.warning(f"Failed password change attempt for: {user.email}")
        raise HTTPException(status_code=401, detail="Current password is incorrect")
    
    # ✅ Validate new password strength
    is_valid, error_msg = validate_password(new_password)
    if not is_valid:
        raise HTTPException(status_code=400, detail=error_msg)
    
    # ✅ Ensure new password is different from current
    if verify_password(new_password, user.password_hash):
        raise HTTPException(status_code=400, detail="New password must be different from current password")
    
    # Update password
    user.password_hash = hash_password(new_password)
    user.updated_at = datetime.utcnow()
    
    session.add(user)
    session.commit()
    
    logger.info(f"✅ Password changed for user: {user.email}")
    
    return {
        "message": "Password changed successfully"
    }


# -----------------------------
# FORGOT PASSWORD
# -----------------------------

@router.post("/forgot-password")
@limiter.limit("3/hour")  # ✅ Prevent abuse
async def forgot_password(
    request: Request,
    data: ForgotPasswordRequest,
    session: Session = Depends(get_session)
):
    """
    Request password reset - sends email with reset link
    """
    email = data.email.strip().lower()
    
    if not email:
        raise HTTPException(status_code=400, detail="Email is required")
    
    # Check if user exists
    user = session.exec(select(User).where(User.email == email)).first()
    
    # Always return success (don't reveal if email exists - security)
    if not user:
        logger.info(f"Password reset requested for non-existent email: {email}")
        return {
            "success": True,
            "message": "If an account exists with that email, a reset link has been sent."
        }
    
    # Generate unique reset token
    reset_token = secrets.token_urlsafe(32)
    expires_at = datetime.utcnow() + timedelta(hours=1)
    
    import sqlite3
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO password_reset_tokens (user_id, token, expires_at)
            VALUES (?, ?, ?)
        """, (user.id, reset_token, expires_at.isoformat()))
        conn.commit()
        logger.info(f"✅ Password reset token created for {user.email}")
    except Exception as e:
        conn.rollback()
        logger.error(f"Error saving reset token: {e}")
        raise HTTPException(status_code=500, detail="Failed to process password reset request")
    finally:
        conn.close()
    
    # Send reset email
    frontend_url = os.getenv("FRONTEND_URL", "http://localhost:5173")
    reset_link = f"{frontend_url}/reset-password?token={reset_token}"
    
    send_password_reset_email(user.email, user.full_name or "User", reset_link)
    
    return {
        "success": True,
        "message": "If an account exists with that email, a reset link has been sent."
    }


# -----------------------------
# VERIFY RESET TOKEN
# -----------------------------

@router.post("/verify-reset-token")
def verify_reset_token(data: VerifyTokenRequest):
    """
    Verify if reset token is valid (before showing reset form)
    """
    token = data.token.strip()
    
    if not token:
        raise HTTPException(status_code=400, detail="Token is required")
    
    import sqlite3
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            SELECT expires_at, used
            FROM password_reset_tokens
            WHERE token = ?
        """, (token,))
        
        result = cursor.fetchone()
        
        if not result:
            return {"valid": False, "message": "Invalid reset token"}
        
        expires_at, used = result
        
        if used:
            return {"valid": False, "message": "This reset link has already been used"}
        
        if datetime.fromisoformat(expires_at) < datetime.utcnow():
            return {"valid": False, "message": "Reset token has expired"}
        
        return {"valid": True, "message": "Token is valid"}
        
    finally:
        conn.close()


# -----------------------------
# RESET PASSWORD
# -----------------------------

@router.post("/reset-password")
@limiter.limit("5/hour")  # ✅ Prevent abuse
async def reset_password(
    request: Request,
    data: ResetPasswordRequest,
    session: Session = Depends(get_session)
):
    """
    Reset password using token from email
    """
    token = data.token.strip()
    new_password = data.password.strip()
    
    if not token:
        raise HTTPException(status_code=400, detail="Reset token is required")
    
    if not new_password:
        raise HTTPException(status_code=400, detail="New password is required")
    
    # ✅ Validate password strength
    is_valid, error_msg = validate_password(new_password)
    if not is_valid:
        raise HTTPException(status_code=400, detail=error_msg)
    
    import sqlite3
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    try:
        # Find valid token
        cursor.execute("""
            SELECT user_id, expires_at, used
            FROM password_reset_tokens
            WHERE token = ?
        """, (token,))
        
        result = cursor.fetchone()
        
        if not result:
            raise HTTPException(status_code=400, detail="Invalid or expired reset token")
        
        user_id, expires_at, used = result
        
        # Check if token already used
        if used:
            raise HTTPException(status_code=400, detail="This reset link has already been used")
        
        # Check if token expired
        if datetime.fromisoformat(expires_at) < datetime.utcnow():
            raise HTTPException(status_code=400, detail="Reset token has expired. Please request a new one.")
        
        # Get user
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Update user password
        user.password_hash = hash_password(new_password)
        user.updated_at = datetime.utcnow()
        session.add(user)
        session.commit()
        
        # Mark token as used
        cursor.execute("""
            UPDATE password_reset_tokens
            SET used = 1
            WHERE token = ?
        """, (token,))
        conn.commit()
        
        logger.info(f"✅ Password reset successful for user: {user.email}")
        
        return {
            "success": True,
            "message": "Password reset successful. You can now login with your new password."
        }
        
    except HTTPException:
        raise
    except Exception as e:
        conn.rollback()
        logger.error(f"Error in reset_password: {e}")
        raise HTTPException(status_code=500, detail="Failed to reset password")
    finally:
        conn.close()
