"""
Settings and preferences management endpoints for authentication
"""
from fastapi import APIRouter, Depends
from sqlmodel import Session
from datetime import datetime

from database import get_session
from models.user import User
from utils.auth import get_current_user

from ._schemas import SettingsUpdate, PreferencesUpdate

router = APIRouter()


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
