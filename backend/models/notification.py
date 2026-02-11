# models/notification.py
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Notification(SQLModel, table=True):
    __tablename__ = "notifications"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    item_id: int = Field(foreign_key="items.id", index=True)
    
    # Notification details
    title: str
    message: str
    notification_type: str = Field(default="expiry_warning")  # expiry_warning, expired, renewal_due
    
    # Status
    is_read: bool = Field(default=False)
    is_sent_via_email: bool = Field(default=False)
    
    # Timestamps
    created_at: datetime = Field(default_factory=datetime.utcnow)
    read_at: Optional[datetime] = None