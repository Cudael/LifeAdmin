# routes/notifications/crud.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from datetime import date, timedelta

from database import get_session
from models.user import User
from utils.auth import get_current_user
from utils.notification_service import (
    mark_notification_read,
    mark_all_read
)

router = APIRouter()


@router.post("/notifications/{notification_id}/read")
@router.post("/notifications/{notification_id}/read/")
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


@router.post("/notifications/mark-all-read")
@router.post("/notifications/mark-all-read/")
def mark_all_as_read(
    user: User = Depends(get_current_user),
    session: Session = Depends(get_session)
):
    """Mark all notifications as read"""
    count = mark_all_read(user.id, session)
    return {"message": f"Marked {count} notifications as read"}


@router.post("/notifications/check-expiring")
@router.post("/notifications/check-expiring/")
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


@router.post("/notifications/test-email")
@router.post("/notifications/test-email/")
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
