# backend/utils/auth.py
from datetime import datetime, timedelta
from typing import Optional
import os
from dotenv import load_dotenv

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
import jwt  # PyJWT library (replaces python-jose to avoid ecdsa vulnerability)
from jwt.exceptions import PyJWTError
from passlib.context import CryptContext
from sqlmodel import Session

from database import get_session
from models.user import User

# ✅ Load environment variables
load_dotenv()

# ✅ Read SECRET_KEY from .env file
SECRET_KEY = os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise ValueError("❌ SECRET_KEY not found! Create a .env file with SECRET_KEY=your-secret-key")

ALGORITHM = "HS256"

# ✅ Token expiration times (configurable via environment variables)
# Access token: Default 30 minutes (recommended for security)
# Refresh token: Default 30 days
DEFAULT_ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
DEFAULT_REFRESH_TOKEN_EXPIRE_DAYS = 30  # 30 days

try:
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", DEFAULT_ACCESS_TOKEN_EXPIRE_MINUTES))
except ValueError:
    raise ValueError("❌ ACCESS_TOKEN_EXPIRE_MINUTES must be a valid integer")

try:
    REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", DEFAULT_REFRESH_TOKEN_EXPIRE_DAYS))
except ValueError:
    raise ValueError("❌ REFRESH_TOKEN_EXPIRE_DAYS must be a valid integer")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Password hashing
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)

# Token creation
def create_access_token(data: dict):
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(data: dict):
    expire = datetime.utcnow() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

# Token verification
def verify_refresh_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

def decode_token(token: str):
    """Decode and verify a JWT token (for OAuth)"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except PyJWTError:
        return None

# Get current user from token
def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: Session = Depends(get_session)
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = int(payload.get("sub"))
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user