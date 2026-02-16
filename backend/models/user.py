# models/user.py
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

    full_name: Optional[str] = None  # Changed to Optional for Google users
    email: str = Field(unique=True, index=True)
    password_hash: Optional[str] = None  # Changed to Optional for Google OAuth users

    # Email verification (NEW)
    email_verified: bool = Field(default=False)
    email_verified_at: Optional[datetime] = None

    # Google OAuth fields
    google_id: Optional[str] = Field(default=None, unique=True, index=True)
    profile_picture: Optional[str] = None

    # Access token (optional — you can remove this later)
    token: Optional[str] = None

    # Refresh token + expiration
    refresh_token: Optional[str] = None
    refresh_token_expires: Optional[datetime] = None

    # Notification preferences
    email_notifications: bool = Field(default=True)  # Enable/disable email notifications
    notification_days_before: int = Field(default=7)  # How many days before expiry to notify (default 7 days)
    daily_digest: bool = Field(default=False)  # Send daily digest email

    # Display preferences
    date_format: str = Field(default="MM/DD/YYYY")  # Date format preference
    time_format: str = Field(default="12h")  # Time format preference (12h or 24h)
    items_per_page: int = Field(default=25)  # Items to show per page
    default_sort: str = Field(default="expiration_asc")  # Default sort order for items list

    # Account settings
    language: str = Field(default="en")  # Language preference
    timezone: str = Field(default="UTC")  # Timezone preference

    # Subscription fields
    stripe_customer_id: Optional[str] = Field(default=None, index=True)
    stripe_subscription_id: Optional[str] = None
    subscription_status: Optional[str] = None  # active, canceled, past_due, trialing
    subscription_plan: str = Field(default="free")  # free, premium
    subscription_current_period_end: Optional[datetime] = None

    # Timestamps
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    
    def is_premium(self) -> bool:
        """Check if user has active premium subscription"""
        return (
            self.subscription_plan == "premium" 
            and self.subscription_status in ["active", "trialing"]
        )
    
    def can_add_items(self, current_item_count: int) -> bool:
        """Check if user can add more items (free users limited to 20)"""
        if self.is_premium():
            return True
        return current_item_count < 20