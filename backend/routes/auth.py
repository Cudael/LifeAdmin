# backend/routes/auth.py
from fastapi import APIRouter, HTTPException, Depends
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
from pydantic import BaseModel
from datetime import datetime, timedelta

router = APIRouter(prefix="/auth", tags=["auth"])


# -----------------------------
# Pydantic Schemas
# -----------------------------

class UserCreate(BaseModel):
    full_name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


# -----------------------------
# REGISTER
# -----------------------------

@router.post("/register")
def register(data: UserCreate, session: Session = Depends(get_session)):
    existing = session.exec(select(User).where(User.email == data.email)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        full_name=data.full_name,
        email=data.email,
        password_hash=hash_password(data.password)
    )

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return {"message": "User registered successfully"}


# -----------------------------
# LOGIN
# -----------------------------

@router.post("/login")
def login(data: UserLogin, session: Session = Depends(get_session)):
    user = session.exec(select(User).where(User.email == data.email)).first()

    if not user or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token({"sub": str(user.id)})
    refresh_token = create_refresh_token({"sub": str(user.id)})

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

@router.post("/refresh")  # Fixed: removed duplicate /auth prefix
def refresh_access_token(body: dict, session: Session = Depends(get_session)):
    refresh_token = body.get("refresh_token")
    
    # Verify the refresh token
    payload = verify_refresh_token(refresh_token)
    user_id = payload.get("sub")
    
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    # ✅ Create NEW access token
    new_access_token = create_access_token({"sub": str(user.id)})
    
    # ✅ Create NEW refresh token (rotation)
    new_refresh_token = create_refresh_token({"sub": str(user.id)})
    
    return {
        "access_token": new_access_token,
        "refresh_token": new_refresh_token  # ✅ Return new refresh token
    }

# -----------------------------
# GET CURRENT USER
# -----------------------------

@router.get("/me")
def get_me(user: User = Depends(get_current_user)):
    return {
        "id": user.id,
        "email": user.email,
        "full_name": user.full_name,
        "username": user.full_name,  # ✅ Added for frontend compatibility
        "profile_picture": user.profile_picture,  # ✅ Added for Google OAuth users
        "created_at": user.created_at.isoformat() if user.created_at else None  # ✅ Added
    }