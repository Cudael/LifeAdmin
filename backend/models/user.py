# models/user.py
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    full_name: Optional[str] = None  # Changed to Optional for Google users
    email: str = Field(unique=True, index=True)
    password_hash: Optional[str] = None  # Changed to Optional for Google OAuth users

    # Google OAuth fields (NEW)
    google_id: Optional[str] = Field(default=None, unique=True, index=True)
    profile_picture: Optional[str] = None

    # Access token (optional — you can remove this later)
    token: Optional[str] = None

    # Refresh token + expiration
    refresh_token: Optional[str] = None
    refresh_token_expires: Optional[datetime] = None

    # Timestamps
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

    # Notification preferences (NEW)
    email_notifications: bool = Field(default=True)  # Enable/disable email notifications
    notification_days_before: int = Field(default=7)  # How many days before expiry to notify (default 7 days)
    daily_digest: bool = Field(default=False)  # Send daily digest email