"""
User registration endpoints
"""
import os
import secrets
import sqlite3
import logging
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, Depends, Request
from sqlmodel import Session, select
from slowapi import Limiter
from slowapi.util import get_remote_address

from database import get_session
from models.user import User
from utils.auth import hash_password, create_access_token, create_refresh_token

from ._schemas import UserCreate
from ._validation import validate_password
from ._email import send_verification_email

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)
logger = logging.getLogger(__name__)


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

    return {
        "message": "User registered successfully. Please check your email to verify your account.",
        "email_sent": True
    }
