# backend/routes/auth.py
from fastapi import APIRouter, HTTPException, Depends, Request
from sqlmodel import Session, select

from database import get_session
from models.user import User
from utils.auth import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    get_current_user,
    verify_refresh_token
)
from pydantic import BaseModel, EmailStr, validator
from typing import Optional
from datetime import datetime, timedelta
import secrets
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import os
import re
import logging

from slowapi import Limiter
from slowapi.util import get_remote_address

router = APIRouter(prefix="/auth", tags=["auth"])
limiter = Limiter(key_func=get_remote_address)
logger = logging.getLogger(__name__)


# -----------------------------
# Password Validation
# -----------------------------

def validate_password(password: str) -> tuple[bool, str]:
    """
    Validate password strength
    Returns: (is_valid, error_message)
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    
    if len(password) > 128:
        return False, "Password must not exceed 128 characters"
    
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter"
    
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter"
    
    if not re.search(r"\d", password):
        return False, "Password must contain at least one number"
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=\[\]\\\/~`]", password):
        return False, "Password must contain at least one special character"
    
    # Check for common passwords
    common_passwords = [
        "password", "12345678", "qwerty", "admin", "letmein",
        "password123", "welcome", "monkey", "dragon", "master"
    ]
    if password.lower() in common_passwords:
        return False, "Password is too common. Please choose a stronger password"
    
    return True, ""


# -----------------------------
# Pydantic Schemas
# -----------------------------

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr  # ✅ Validates email format
    password: str
    
    @validator('full_name')
    def validate_name(cls, v):
        if not v or len(v.strip()) < 2:
            raise ValueError('Name must be at least 2 characters long')
        if len(v) > 100:
            raise ValueError('Name must not exceed 100 characters')
        return v.strip()
    
    @validator('email')
    def validate_email(cls, v):
        # Check for disposable email domains
        disposable_domains = [
            'tempmail.com', 'throwaway.email', '10minutemail.com',
            'guerrillamail.com', 'mailinator.com', 'trashmail.com'
        ]
        domain = v.split('@')[1].lower()
        if domain in disposable_domains:
            raise ValueError('Disposable email addresses are not allowed')
        return v.lower()


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    token: str
    password: str


class VerifyTokenRequest(BaseModel):
    token: str


class PreferencesUpdate(BaseModel):
    """Validated user display preferences"""
    date_format: Optional[str] = None
    time_format: Optional[str] = None
    items_per_page: Optional[int] = None
    default_sort: Optional[str] = None
    
    @validator('date_format')
    def validate_date_format(cls, v):
        if v is not None:
            allowed_formats = ['MM/DD/YYYY', 'DD/MM/YYYY', 'YYYY-MM-DD', 'DD.MM.YYYY']
            if v not in allowed_formats:
                raise ValueError(f'Invalid date format. Allowed: {", ".join(allowed_formats)}')
        return v
    
    @validator('time_format')
    def validate_time_format(cls, v):
        if v is not None:
            allowed_formats = ['12h', '24h']
            if v not in allowed_formats:
                raise ValueError(f'Invalid time format. Allowed: {", ".join(allowed_formats)}')
        return v
    
    @validator('items_per_page')
    def validate_items_per_page(cls, v):
        if v is not None:
            if v < 5 or v > 100:
                raise ValueError('Items per page must be between 5 and 100')
        return v
    
    @validator('default_sort')
    def validate_default_sort(cls, v):
        if v is not None:
            allowed_sorts = ['expiration_asc', 'expiration_desc', 'title_asc', 'title_desc', 'created_asc', 'created_desc']
            if v not in allowed_sorts:
                raise ValueError(f'Invalid sort option. Allowed: {", ".join(allowed_sorts)}')
        return v


class SettingsUpdate(BaseModel):
    """Validated user account settings"""
    email_notifications_enabled: Optional[bool] = None
    notification_days: Optional[int] = None
    daily_digest: Optional[bool] = None
    language: Optional[str] = None
    timezone: Optional[str] = None
    
    @validator('notification_days')
    def validate_notification_days(cls, v):
        if v is not None:
            if v < 0 or v > 365:
                raise ValueError('Notification days must be between 0 and 365')
        return v
    
    @validator('language')
    def validate_language(cls, v):
        if v is not None:
            # Common language codes
            allowed_languages = ['en', 'es', 'fr', 'de', 'it', 'pt', 'ja', 'zh', 'ko', 'ar', 'ru']
            if v not in allowed_languages:
                raise ValueError(f'Invalid language code. Allowed: {", ".join(allowed_languages)}')
        return v
    
    @validator('timezone')
    def validate_timezone(cls, v):
        if v is not None:
            # Basic validation - accept common patterns
            # For stricter validation, install pytz: pip install pytz
            # and use: pytz.timezone(v) to validate
            if len(v) > 50 or len(v) < 3:
                raise ValueError('Invalid timezone string')
            # Basic format check (e.g., "UTC", "America/New_York")
            if not v.replace('_', '').replace('/', '').replace('-', '').replace('+', '').isalnum():
                raise ValueError('Invalid timezone format')
        return v


# -----------------------------
# REGISTER
# -----------------------------

@router.post("/register")
@limiter.limit("5/hour")  # ✅ Max 5 registrations per hour per IP
async def register(
    request: Request,
    data: UserCreate,
    session: Session = Depends(get_session)
):
    """Register a new user account"""
    
    # ✅ Validate password strength
    is_valid, error_msg = validate_password(data.password)
    if not is_valid:
        logger.warning(f"Weak password attempt for email: {data.email}")
        raise HTTPException(status_code=400, detail=error_msg)
    
    # Check if email already exists
    existing = session.exec(select(User).where(User.email == data.email)).first()
    if existing:
        logger.warning(f"Registration attempt with existing email: {data.email}")
        raise HTTPException(status_code=400, detail="Email already registered")

    # Create new user
    new_user = User(
        full_name=data.full_name,
        email=data.email,
        password_hash=hash_password(data.password),
        email_verified=False
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    
    logger.info(f"✅ New user registered: {new_user.email}")
    
    # Generate verification token
    verification_token = secrets.token_urlsafe(32)
    expires_at = datetime.utcnow() + timedelta(hours=24)
    
    # Save token to database
    import sqlite3
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("""
            INSERT INTO email_verification_tokens (user_id, token, expires_at)
            VALUES (?, ?, ?)
        """, (new_user.id, verification_token, expires_at.isoformat()))
        conn.commit()
        logger.info(f"✅ Verification token created for {new_user.email}")
    except Exception as e:
        logger.error(f"⚠️ Error saving verification token: {e}")
    finally:
        conn.close()
    
    # Send verification email
    frontend_url = os.getenv("FRONTEND_URL", "http://localhost:5173")
    verification_link = f"{frontend_url}/verify-email?token={verification_token}"
    
    send_verification_email(new_user.email, new_user.full_name, verification_link)

    # Generate tokens for immediate login after registration
    access_token = create_access_token(data={"sub": str(new_user.id)})
    refresh_token_val = create_refresh_token(data={"sub": str(new_user.id)})

    return {
        "message": "User registered successfully. Please check your email to verify your account.",
        "email_sent": True,
        "access_token": access_token,
        "refresh_token": refresh_token_val,
        "user": {
            "id": new_user.id,
            "email": new_user.email,
            "full_name": new_user.full_name,
            "email_verified": new_user.email_verified
        }
    }


# -----------------------------
# LOGIN
# -----------------------------

@router.post("/login")
@limiter.limit("10/minute")  # ✅ Max 10 login attempts per minute per IP
async def login(
    request: Request,
    data: UserLogin,
    session: Session = Depends(get_session)
):
    """Authenticate user and return access token"""
    
    user = session.exec(select(User).where(User.email == data.email)).first()

    if not user or not user.password_hash or not verify_password(data.password, user.password_hash):
        logger.warning(f"Failed login attempt for: {data.email} from {request.client.host}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    logger.info(f"✅ Successful login: {user.email}")

    access_token = create_access_token({"sub": str(user.id)})
    refresh_token = create_refresh_token({"sub": str(user.id)})

    # ✅ Update refresh token in database
    user.refresh_token = refresh_token
    user.refresh_token_expires = datetime.utcnow() + timedelta(days=30)

    session.add(user)
    session.commit()

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer"
    }


# -----------------------------
# REFRESH TOKEN
# -----------------------------

@router.post("/refresh")
@limiter.limit("20/minute")  # ✅ Prevent refresh token abuse
async def refresh_access_token(
    request: Request,
    body: dict,
    session: Session = Depends(get_session)
):
    """Refresh access token using refresh token"""
    
    refresh_token = body.get("refresh_token")
    
    if not refresh_token:
        raise HTTPException(status_code=400, detail="Refresh token is required")
    
    # Verify the refresh token
    payload = verify_refresh_token(refresh_token)
    user_id = payload.get("sub")
    
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    # ✅ Verify the refresh token matches the one in database
    if user.refresh_token != refresh_token:
        logger.warning(f"Invalid refresh token attempt for user: {user.email}")
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    
    # ✅ Check if refresh token expired
    if user.refresh_token_expires and user.refresh_token_expires < datetime.utcnow():
        logger.warning(f"Expired refresh token for user: {user.email}")
        raise HTTPException(status_code=401, detail="Refresh token expired")
    
    # Create NEW tokens (rotation)
    new_access_token = create_access_token({"sub": str(user.id)})
    new_refresh_token = create_refresh_token({"sub": str(user.id)})
    
    # ✅ Update refresh token in database
    user.refresh_token = new_refresh_token
    user.refresh_token_expires = datetime.utcnow() + timedelta(days=30)
    session.add(user)
    session.commit()
    
    logger.info(f"✅ Token refreshed for user: {user.email}")
    
    return {
        "access_token": new_access_token,
        "refresh_token": new_refresh_token
    }


# -----------------------------
# GET CURRENT USER PROFILE
# -----------------------------

@router.get("/me")
def get_me(user: User = Depends(get_current_user)):
    """Get current user's profile information"""
    return {
        "id": user.id,
        "email": user.email,
        "full_name": user.full_name,
        "name": user.full_name,
        "username": user.full_name,
        "profile_picture": user.profile_picture,
        "email_verified": user.email_verified,
        "created_at": user.created_at.isoformat() if user.created_at else None,
        "updated_at": user.updated_at.isoformat() if user.updated_at else None
    }


# -----------------------------
# UPDATE USER PROFILE
# -----------------------------

@router.put("/me")
def update_profile(
    profile_data: dict,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Update current user's profile (name only)"""
    
    if "full_name" in profile_data:
        full_name = profile_data["full_name"].strip()
        if len(full_name) < 2:
            raise HTTPException(status_code=400, detail="Name must be at least 2 characters long")
        if len(full_name) > 100:
            raise HTTPException(status_code=400, detail="Name must not exceed 100 characters")
        user.full_name = full_name
    
    user.updated_at = datetime.utcnow()
    
    session.add(user)
    session.commit()
    session.refresh(user)
    
    logger.info(f"✅ Profile updated for user: {user.email}")
    
    return {
        "message": "Profile updated successfully",
        "updated_at": user.updated_at.isoformat()
    }


# -----------------------------
# DELETE ACCOUNT
# -----------------------------

@router.delete("/me")
@limiter.limit("3/hour")  # ✅ Prevent abuse of account deletion
async def delete_account(
    request: Request,
    password_data: dict,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """
    Delete user account and all associated data (GDPR compliance)
    """
    password = password_data.get("password", "").strip()
    
    if not password:
        raise HTTPException(status_code=400, detail="Password is required to delete account")
    
    # Verify password
    if not user.password_hash or not verify_password(password, user.password_hash):
        logger.warning(f"Failed account deletion attempt for: {user.email}")
        raise HTTPException(status_code=401, detail="Incorrect password")
    
    user_id = user.id
    user_email = user.email
    
    # Import Item model
    from models.item import Item
    import sqlite3
    
    try:
        # 1. Get all user's items
        items = session.exec(select(Item).where(Item.user_id == user_id)).all()
        
        # 2. Delete all associated files
        files_deleted = 0
        for item in items:
            if item.file_path:
                file_path = f"uploads/{item.file_path}"
                if os.path.exists(file_path):
                    try:
                        os.remove(file_path)
                        files_deleted += 1
                    except Exception as e:
                        logger.error(f"⚠️ Could not delete file {file_path}: {e}")
        
        # 3. Delete all user's items
        for item in items:
            session.delete(item)
        
        items_deleted = len(items)
        
        # 4. Delete tokens
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM password_reset_tokens WHERE user_id = ?", (user_id,))
            cursor.execute("DELETE FROM email_verification_tokens WHERE user_id = ?", (user_id,))
            conn.commit()
        except Exception as e:
            logger.error(f"⚠️ Could not delete tokens: {e}")
        finally:
            conn.close()
        
        # 5. Delete user profile picture if exists
        if user.profile_picture:
            profile_pic_path = f"uploads/{user.profile_picture}"
            if os.path.exists(profile_pic_path):
                try:
                    os.remove(profile_pic_path)
                except Exception as e:
                    logger.error(f"⚠️ Could not delete profile picture: {e}")
        
        # 6. Delete the user account
        session.delete(user)
        session.commit()
        
        logger.info(f"""
        ╔════════════════════════════════════════╗
        ║   ACCOUNT DELETED                      ║
        ╠════════════════════════════════��═══════╣
        ║ Email: {user_email:<30} ║
        ║ Items deleted: {items_deleted:<23} ║
        ║ Files deleted: {files_deleted:<23} ║
        ╚════════════════════════════════════════╝
        """)
        
        return {
            "success": True,
            "message": "Account deleted successfully",
            "items_deleted": items_deleted,
            "files_deleted": files_deleted
        }
        
    except Exception as e:
        session.rollback()
        logger.error(f"❌ Error deleting account: {e}")
        raise HTTPException(status_code=500, detail="Failed to delete account. Please contact support.")


# -----------------------------
# VERIFY EMAIL
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


# -----------------------------
# GET ACCOUNT SETTINGS
# -----------------------------

@router.get("/settings")
def get_settings(user: User = Depends(get_current_user)):
    """Get user account settings (notifications, language, timezone)"""
    return {
        "email_notifications_enabled": user.email_notifications,
        "notification_days": user.notification_days_before,
        "daily_digest": user.daily_digest,
        "language": user.language,
        "timezone": user.timezone
    }


# -----------------------------
# UPDATE ACCOUNT SETTINGS
# -----------------------------

@router.put("/settings")
def update_settings(
    settings_data: SettingsUpdate,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Update user account settings"""
    
    if settings_data.email_notifications_enabled is not None:
        user.email_notifications = settings_data.email_notifications_enabled
    if settings_data.notification_days is not None:
        user.notification_days_before = settings_data.notification_days
    if settings_data.daily_digest is not None:
        user.daily_digest = settings_data.daily_digest
    if settings_data.language is not None:
        user.language = settings_data.language
    if settings_data.timezone is not None:
        user.timezone = settings_data.timezone
    
    user.updated_at = datetime.utcnow()
    
    session.add(user)
    session.commit()
    session.refresh(user)
    
    return {
        "message": "Settings updated successfully"
    }


# -----------------------------
# GET DISPLAY PREFERENCES
# -----------------------------

@router.get("/preferences")
def get_preferences(user: User = Depends(get_current_user)):
    """Get user display preferences (date format, sorting, items per page)"""
    return {
        "date_format": user.date_format,
        "time_format": user.time_format,
        "items_per_page": user.items_per_page,
        "default_sort": user.default_sort
    }


# -----------------------------
# UPDATE DISPLAY PREFERENCES
# -----------------------------

@router.put("/preferences")
def update_preferences(
    preferences_data: PreferencesUpdate,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Update user display preferences"""
    
    if preferences_data.date_format is not None:
        user.date_format = preferences_data.date_format
    if preferences_data.time_format is not None:
        user.time_format = preferences_data.time_format
    if preferences_data.items_per_page is not None:
        user.items_per_page = preferences_data.items_per_page
    if preferences_data.default_sort is not None:
        user.default_sort = preferences_data.default_sort
    
    user.updated_at = datetime.utcnow()
    
    session.add(user)
    session.commit()
    session.refresh(user)
    
    return {
        "message": "Preferences updated successfully",
        "date_format": user.date_format,
        "time_format": user.time_format,
        "items_per_page": user.items_per_page,
        "default_sort": user.default_sort
    }


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


# -----------------------------
# EMAIL HELPERS
# -----------------------------

def send_password_reset_email(to_email: str, user_name: str, reset_link: str):
    """Send password reset email"""
    smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER", "")
    smtp_password = os.getenv("SMTP_PASSWORD", "")
    from_email = os.getenv("FROM_EMAIL", smtp_user)
    
    if not smtp_user or not smtp_password:
        logger.info(f"\n{'='*60}\n📧 PASSWORD RESET EMAIL (SMTP not configured)\n{'='*60}\nTo: {to_email}\nReset Link: {reset_link}\n{'='*60}\n")
        return
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Reset Your Remindes Password'
    msg['From'] = from_email
    msg['To'] = to_email
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: linear-gradient(135deg, #14b8a6 0%, #06b6d4 100%); 
                       color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0; }}
            .content {{ background: #f9f9f9; padding: 30px; border-radius: 0 0 10px 10px; }}
            .button {{ display: inline-block; padding: 15px 30px; background: linear-gradient(135deg, #14b8a6 0%, #06b6d4 100%); 
                       color: white; text-decoration: none; border-radius: 8px; font-weight: bold; margin: 20px 0; }}
            .footer {{ text-align: center; margin-top: 20px; color: #666; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🔑 Password Reset Request</h1>
            </div>
            <div class="content">
                <p>Hi {user_name},</p>
                <p>We received a request to reset your Remindes password. Click the button below to create a new password:</p>
                <div style="text-align: center;">
                    <a href="{reset_link}" class="button">Reset Password</a>
                </div>
                <p>Or copy and paste this link into your browser:</p>
                <p style="background: white; padding: 15px; border-radius: 5px; word-break: break-all; font-size: 14px;">
                    {reset_link}
                </p>
                <p><strong>⏰ This link will expire in 1 hour.</strong></p>
                <p>If you didn't request a password reset, you can safely ignore this email.</p>
                <p>Best regards,<br>The Remindes Team</p>
            </div>
            <div class="footer">
                <p>This is an automated email. Please do not reply.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    msg.attach(MIMEText(html, 'html'))
    
    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
        logger.info(f"✅ Password reset email sent to {to_email}")
    except Exception as e:
        logger.error(f"❌ Failed to send email: {e}")


def send_verification_email(to_email: str, user_name: str, verification_link: str):
    """Send email verification link"""
    smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER", "")
    smtp_password = os.getenv("SMTP_PASSWORD", "")
    from_email = os.getenv("FROM_EMAIL", smtp_user)
    
    if not smtp_user or not smtp_password:
        logger.info(f"\n{'='*60}\n📧 EMAIL VERIFICATION (SMTP not configured)\n{'='*60}\nTo: {to_email}\nVerification Link: {verification_link}\n{'='*60}\n")
        return
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Verify Your Remindes Email Address'
    msg['From'] = from_email
    msg['To'] = to_email
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 600px; margin: 0 auto; padding: 20px; }}
            .header {{ background: linear-gradient(135deg, #14b8a6 0%, #06b6d4 100%); 
                       color: white; padding: 30px; text-align: center; border-radius: 10px 10px 0 0; }}
            .content {{ background: #f9f9f9; padding: 30px; border-radius: 0 0 10px 10px; }}
            .button {{ display: inline-block; padding: 15px 30px; background: linear-gradient(135deg, #14b8a6 0%, #06b6d4 100%); 
                       color: white; text-decoration: none; border-radius: 8px; font-weight: bold; margin: 20px 0; }}
            .footer {{ text-align: center; margin-top: 20px; color: #666; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>✉️ Verify Your Email</h1>
            </div>
            <div class="content">
                <p>Hi {user_name},</p>
                <p>Welcome to Remindes! Please verify your email address to get started:</p>
                <div style="text-align: center;">
                    <a href="{verification_link}" class="button">Verify Email Address</a>
                </div>
                <p>Or copy and paste this link into your browser:</p>
                <p style="background: white; padding: 15px; border-radius: 5px; word-break: break-all; font-size: 14px;">
                    {verification_link}
                </p>
                <p><strong>⏰ This link will expire in 24 hours.</strong></p>
                <p>If you didn't create an account, you can safely ignore this email.</p>
                <p>Best regards,<br>The Remindes Team</p>
            </div>
            <div class="footer">
                <p>This is an automated email. Please do not reply.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    msg.attach(MIMEText(html, 'html'))
    
    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)
        logger.info(f"✅ Verification email sent to {to_email}")
    except Exception as e:
        logger.error(f"❌ Failed to send email: {e}")