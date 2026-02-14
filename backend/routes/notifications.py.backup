# routes/notifications.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List
from pydantic import BaseModel
from datetime import date, timedelta

from database import get_session
from models.notification import Notification
from models.user import User
from utils.auth import get_current_user
from utils.notification_service import (
    get_user_notifications,
    mark_notification_read,
    mark_all_read
)

router = APIRouter(prefix="/notifications", tags=["Notifications"])


class NotificationResponse(BaseModel):
    id: int
    title: str
    message: str
    notification_type: str
    is_read: bool
    created_at: str
    item_id: int


@router.get("/", response_model=List[NotificationResponse])
def get_notifications(
    unread_only: bool = False,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Get all notifications for the current user"""
    notifications = get_user_notifications(user.id, session, unread_only)
    
    return [
        NotificationResponse(
            id=n.id,
            title=n.title,
            message=n.message,
            notification_type=n.notification_type,
            is_read=n.is_read,
            created_at=n.created_at.isoformat(),
            item_id=n.item_id
        )
        for n in notifications
    ]


@router.get("/unread-count")
def get_unread_count(
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Get count of unread notifications"""
    notifications = get_user_notifications(user.id, session, unread_only=True)
    return {"count": len(notifications)}


@router.post("/{notification_id}/read")
def mark_as_read(
    notification_id: int,
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Mark a notification as read"""
    success = mark_notification_read(notification_id, user.id, session)
    
    if not success:
        raise HTTPException(status_code=404, detail="Notification not found")
    
    return {"message": "Notification marked as read"}


@router.post("/mark-all-read")
def mark_all_as_read(
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Mark all notifications as read"""
    count = mark_all_read(user.id, session)
    return {"message": f"Marked {count} notifications as read"}


@router.post("/check-expiring")
def trigger_expiry_check(
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Manually trigger expiry check (for testing)"""
    from utils.notification_service import check_expiring_items
    
    count = check_expiring_items(session)
    return {
        "message": "Expiry check completed",
        "notifications_created": count
    }


@router.post("/test-email")
def test_email(
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Test email sending (for debugging)"""
    from utils.email_service import send_expiry_notification_email
    
    print(f"🧪 Testing email for user: {user.email}")
    
    # Send a test email
    success = send_expiry_notification_email(
        to_email=user.email,
        user_name=user.full_name or "User",
        item_name="Test Document",
        item_type="Document",
        expiry_date=date.today() + timedelta(days=3),
        days_until_expiry=3
    )
    
    if success:
        return {
            "success": True,
            "message": "✅ Test email sent successfully! Check your inbox (and spam folder).",
            "email": user.email
        }
    else:
        return {
            "success": False,
            "message": "❌ Failed to send email. Check backend logs for detailed error.",
            "email": user.email
        }