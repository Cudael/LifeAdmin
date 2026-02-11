# utils/notification_service.py
from datetime import datetime, timedelta, date
from sqlmodel import Session, select
from models.item import Item
from models.notification import Notification
from models.user import User
from utils.email_service import send_expiry_notification_email, send_expired_notification_email

def check_expiring_items(session: Session):
    """
    Check for items expiring soon and create notifications
    Called by a scheduled job (daily)
    """
    users = session.exec(select(User).where(User.email_notifications == True)).all()
    
    notifications_created = 0
    emails_sent = 0
    
    for user in users:
        # Calculate the threshold date based on user preference
        threshold_date = date.today() + timedelta(days=user.notification_days_before)
        
        # Find ALL items for this user
        statement = select(Item).where(Item.user_id == user.id)
        all_items = session.exec(statement).all()
        
        for item in all_items:
            expiry = item.get_expiry_date()
            
            if not expiry:
                continue  # Skip items without expiry dates
            
            # Check if expiring soon
            if date.today() <= expiry <= threshold_date:
                # Check if notification already exists for this item
                existing = session.exec(
                    select(Notification).where(
                        Notification.user_id == user.id,
                        Notification.item_id == item.id,
                        Notification.notification_type == "expiry_warning",
                        Notification.created_at >= datetime.utcnow() - timedelta(days=1)
                    )
                ).first()
                
                if existing:
                    continue  # Don't create duplicate notifications
                
                # Calculate days until expiry
                days_until_expiry = (expiry - date.today()).days
                
                # Determine the message based on item type
                if item.type == "document":
                    item_description = f"document '{item.name}'"
                elif item.type == "subscription":
                    item_description = f"subscription '{item.name}'"
                else:
                    item_description = f"item '{item.name}'"
                
                # Create notification
                notification = Notification(
                    user_id=user.id,
                    item_id=item.id,
                    title=f"⚠️ {item.name} expiring soon",
                    message=f"Your {item_description} expires in {days_until_expiry} day{'s' if days_until_expiry != 1 else ''}.",
                    notification_type="expiry_warning",
                    is_sent_via_email=False
                )
                
                session.add(notification)
                session.commit()
                session.refresh(notification)
                notifications_created += 1
                
                # Send email if user has email notifications enabled
                if user.email_notifications and user.email:
                    email_sent = send_expiry_notification_email(
                        to_email=user.email,
                        user_name=user.full_name or "User",
                        item_name=item.name,
                        item_type=item.type.capitalize(),
                        expiry_date=expiry,
                        days_until_expiry=days_until_expiry
                    )
                    
                    if email_sent:
                        notification.is_sent_via_email = True
                        session.add(notification)
                        session.commit()
                        emails_sent += 1
            
            # Check if expired
            elif expiry < date.today():
                # Check if already notified about expiry
                existing = session.exec(
                    select(Notification).where(
                        Notification.user_id == user.id,
                        Notification.item_id == item.id,
                        Notification.notification_type == "expired",
                        Notification.created_at >= datetime.utcnow() - timedelta(days=7)
                    )
                ).first()
                
                if existing:
                    continue
                
                days_expired = (date.today() - expiry).days
                
                # Determine the message based on item type
                if item.type == "document":
                    item_description = f"document '{item.name}'"
                elif item.type == "subscription":
                    item_description = f"subscription '{item.name}'"
                else:
                    item_description = f"item '{item.name}'"
                
                notification = Notification(
                    user_id=user.id,
                    item_id=item.id,
                    title=f"❌ {item.name} has expired",
                    message=f"Your {item_description} expired {days_expired} day{'s' if days_expired != 1 else ''} ago.",
                    notification_type="expired",
                    is_sent_via_email=False
                )
                
                session.add(notification)
                session.commit()
                session.refresh(notification)
                notifications_created += 1
                
                # Send email if user has email notifications enabled
                if user.email_notifications and user.email:
                    email_sent = send_expired_notification_email(
                        to_email=user.email,
                        user_name=user.full_name or "User",
                        item_name=item.name,
                        item_type=item.type.capitalize(),
                        expiry_date=expiry,
                        days_expired=days_expired
                    )
                    
                    if email_sent:
                        notification.is_sent_via_email = True
                        session.add(notification)
                        session.commit()
                        emails_sent += 1
    
    print(f"✅ Created {notifications_created} notifications, sent {emails_sent} emails")
    return notifications_created


# Keep the rest of the functions the same...
def get_user_notifications(user_id: int, session: Session, unread_only: bool = False):
    """Get notifications for a user"""
    statement = select(Notification).where(Notification.user_id == user_id)
    
    if unread_only:
        statement = statement.where(Notification.is_read == False)
    
    statement = statement.order_by(Notification.created_at.desc())
    
    return session.exec(statement).all()


def mark_notification_read(notification_id: int, user_id: int, session: Session):
    """Mark a notification as read"""
    notification = session.get(Notification, notification_id)
    
    if not notification or notification.user_id != user_id:
        return False
    
    notification.is_read = True
    notification.read_at = datetime.utcnow()
    session.add(notification)
    session.commit()
    
    return True


def mark_all_read(user_id: int, session: Session):
    """Mark all notifications as read for a user"""
    notifications = session.exec(
        select(Notification).where(
            Notification.user_id == user_id,
            Notification.is_read == False
        )
    ).all()
    
    for notification in notifications:
        notification.is_read = True
        notification.read_at = datetime.utcnow()
        session.add(notification)
    
    session.commit()
    return len(notifications)