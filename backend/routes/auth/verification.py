# backend/routes/auth/verification.py
from fastapi import APIRouter, HTTPException, Depends, Request
from sqlmodel import Session
from database import get_session
from models.user import User
from utils.auth import get_current_user
from datetime import datetime, timedelta
import secrets
import os
import logging

from slowapi import Limiter
from slowapi.util import get_remote_address

from ._email import send_verification_email

router = APIRouter(prefix="/auth", tags=["auth"])
limiter = Limiter(key_func=get_remote_address)
logger = logging.getLogger(__name__)


# -----------------------------
# EMAIL VERIFICATION
# -----------------------------

@router.post("/verify-email")
def verify_email(data: dict, session: Session = Depends(get_session)):
    """
    Verify user's email address using token from email
    """
    token = data.get("token", "").strip()
    
    if not token:
        raise HTTPException(status_code=400, detail="Verification token is required")
    
    import sqlite3
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    try:
        # Find valid token
        cursor.execute("""
            SELECT user_id, expires_at, used
            FROM email_verification_tokens
            WHERE token = ?
        """, (token,))
        
        result = cursor.fetchone()
        
        if not result:
            raise HTTPException(status_code=400, detail="Invalid verification token")
        
        user_id, expires_at, used = result
        
        # Check if already used
        if used:
            raise HTTPException(status_code=400, detail="This verification link has already been used")
        
        # Check if expired
        if datetime.fromisoformat(expires_at) < datetime.utcnow():
            raise HTTPException(status_code=400, detail="Verification link has expired")
        
        # Get user
        user = session.get(User, user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        # Mark email as verified
        user.email_verified = True
        user.email_verified_at = datetime.utcnow()
        session.add(user)
        session.commit()
        
        # Mark token as used
        cursor.execute("""
            UPDATE email_verification_tokens
            SET used = 1
            WHERE token = ?
        """, (token,))
        conn.commit()
        
        logger.info(f"✅ Email verified for user: {user.email}")
        
        return {
            "success": True,
            "message": "Email verified successfully!"
        }
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"❌ Error verifying email: {e}")
        raise HTTPException(status_code=500, detail="Failed to verify email")
    finally:
        conn.close()


# -----------------------------
# RESEND VERIFICATION EMAIL
# -----------------------------

@router.post("/resend-verification")
@limiter.limit("3/hour")  # ✅ Prevent spam
async def resend_verification(
    request: Request,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Resend email verification link
    """
    # Check if already verified
    if user.email_verified:
        raise HTTPException(status_code=400, detail="Email is already verified")
    
    # Generate new token
    verification_token = secrets.token_urlsafe(32)
    expires_at = datetime.utcnow() + timedelta(hours=24)
    
    import sqlite3
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    try:
        # Invalidate old tokens
        cursor.execute("""
            UPDATE email_verification_tokens
            SET used = 1
            WHERE user_id = ? AND used = 0
        """, (user.id,))
        
        # Insert new token
        cursor.execute("""
            INSERT INTO email_verification_tokens (user_id, token, expires_at)
            VALUES (?, ?, ?)
        """, (user.id, verification_token, expires_at.isoformat()))
        
        conn.commit()
        logger.info(f"✅ New verification token created for {user.email}")
    except Exception as e:
        conn.rollback()
        logger.error(f"❌ Error creating verification token: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate verification link")
    finally:
        conn.close()
    
    # Send verification email
    frontend_url = os.getenv("FRONTEND_URL", "http://localhost:5173")
    verification_link = f"{frontend_url}/verify-email?token={verification_token}"
    
    send_verification_email(user.email, user.full_name, verification_link)
    
    return {
        "success": True,
        "message": "Verification email sent!"
    }
