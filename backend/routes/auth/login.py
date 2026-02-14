"""
Login and token management endpoints
"""
import logging
from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, Depends, Request
from sqlmodel import Session, select
from slowapi import Limiter
from slowapi.util import get_remote_address

from database import get_session
from models.user import User
from utils.auth import verify_password, create_access_token, create_refresh_token, verify_refresh_token

from ._schemas import UserLogin

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)
logger = logging.getLogger(__name__)


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
