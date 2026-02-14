"""
Profile management endpoints for authentication
"""
from fastapi import APIRouter, HTTPException, Depends, Request
from sqlmodel import Session, select
from datetime import datetime
import os
import logging
import sqlite3

from database import get_session
from models.user import User
from models.item import Item
from utils.auth import (
    verify_password,
    get_current_user
)
from slowapi import Limiter
from slowapi.util import get_remote_address

from ._validation import validate_password

router = APIRouter()
limiter = Limiter(key_func=get_remote_address)
logger = logging.getLogger(__name__)


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
        ╠════════════════════════════════════════╣
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
