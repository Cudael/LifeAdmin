# routes/notifications/list.py
from fastapi import APIRouter, Depends
from sqlmodel import Session
from typing import List
from pydantic import BaseModel

from database import get_session
from models.user import User
from utils.auth import get_current_user
from utils.notification_service import get_user_notifications

router = APIRouter()


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
