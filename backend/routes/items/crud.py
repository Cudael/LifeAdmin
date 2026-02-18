# backend/routes/items/crud.py
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, Request
from sqlmodel import Session
from typing import Optional
from datetime import datetime
import os
import logging
import json

from slowapi import Limiter
from slowapi.util import get_remote_address

from models.item import Item, ItemCreate, ItemUpdate
from models.user import User
from database import get_session
from utils.auth import get_current_user
from utils.dates import parse_date
from utils.file import save_upload
from utils.file_validation import validate_file
from utils.item_validation import validate_item_fields

router = APIRouter()
logger = logging.getLogger(__name__)
limiter = Limiter(key_func=get_remote_address)


def require_verified_email(user: User = Depends(get_current_user)) -> User:
    """
    Dependency that requires user to have verified email
    """
    if not user.email_verified:
        logger.warning(f"Unverified user attempted write operation: {user.email}")
        raise HTTPException(
            status_code=403,
            detail="Email verification required. Please verify your email to perform this action."
        )
    return user


@router.post("/items")
@router.post("/items/")
@limiter.limit("30/minute")
async def create_item(
    request: Request,
    item: ItemCreate,
    session: Session = Depends(get_session),
    user: User = Depends(require_verified_email)
):
    """Create a new item (JSON payload)"""
    # Check item count limit for free users
    from sqlmodel import select, func
    statement = select(func.count(Item.id)).where(Item.user_id == user.id)
    item_count = session.exec(statement).one()
    
    if not user.can_add_items(item_count):
        logger.warning(f"⚠️ Free user {user.email} attempted to exceed 20 item limit")
        raise HTTPException(
            status_code=403,
            detail="Free plan limited to 20 items. Upgrade to Premium for unlimited items."
        )
    
    db_item = Item.from_orm(item)
    db_item.user_id = user.id
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    
    logger.info(f"✅ Item created: {db_item.id} by user {user.email}")
    return db_item


@router.get("/items/{item_id}")
@router.get("/items/{item_id}/")
def get_item(
    item_id: int,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    """Get a specific item by ID"""
    item = session.get(Item, item_id)
    
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    if item.user_id != user.id:
        logger.warning(f"⚠️ User {user.email} attempted to access item {item_id} owned by another user")
        raise HTTPException(status_code=404, detail="Item not found")
    
    return item


@router.patch("/items/{item_id}")
@router.patch("/items/{item_id}/")
def update_item(
    item_id: int,
    item: ItemUpdate,
    session: Session = Depends(get_session),
    user: User = Depends(require_verified_email)
):
    """Partially update an item (JSON payload)"""
    db_item = session.get(Item, item_id)
    
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    if db_item.user_id != user.id:
        logger.warning(f"⚠️ User {user.email} attempted to update item {item_id} owned by another user")
        raise HTTPException(status_code=403, detail="Not authorized to update this item")

    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)

    db_item.updated_at = datetime.utcnow()
    
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    
    logger.info(f"✅ Item updated: {db_item.id} by user {user.email}")
    return db_item


@router.put("/items/{item_id}")
@router.put("/items/{item_id}/")
@limiter.limit("30/minute")
async def update_item_with_file(
    request: Request,
    item_id: int,
    name: str = Form(...),
    type: str = Form(...),
    category: str = Form(...),
    expiration_date: Optional[str] = Form(None),
    renewal_date: Optional[str] = Form(None),
    notes: Optional[str] = Form(None),
    billing_cycle: Optional[str] = Form(None),
    price: Optional[float] = Form(None),
    document_number: Optional[str] = Form(None),
    reminder_days_before: Optional[int] = Form(None),
    file: UploadFile = File(None),
    session: Session = Depends(get_session),
    user: User = Depends(require_verified_email)
):
    """
    Update an existing item (with optional file upload)
    Used by EditItemPage.vue
    """
    # Get the item
    db_item = session.get(Item, item_id)
    
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Check ownership
    if db_item.user_id != user.id:
        logger.warning(f"⚠️ User {user.email} attempted to update item {item_id} owned by another user")
        raise HTTPException(status_code=403, detail="Not authorized to update this item")
    
    # Validate input
    if len(name) > 200:
        raise HTTPException(status_code=400, detail="Name must not exceed 200 characters")
    
    validate_item_fields(name, type, category)
    
    # Validate file if provided
    if file and file.filename:
        is_valid, error_msg = validate_file(file)
        if not is_valid:
            raise HTTPException(status_code=400, detail=error_msg)
    
    # Update basic fields
    db_item.name = name.strip()
    db_item.type = type
    db_item.category = category
    db_item.notes = notes.strip() if notes else None
    db_item.document_number = document_number.strip() if document_number else None
    
    # Update subscription fields
    db_item.billing_cycle = billing_cycle if billing_cycle else None
    db_item.price = price if price else None
    
    # Update reminder settings
    db_item.reminder_days_before = reminder_days_before
    
    # Handle dates (convert empty strings to None)
    db_item.expiration_date = parse_date(expiration_date) if expiration_date else None
    db_item.renewal_date = parse_date(renewal_date) if renewal_date else None
    
    # Handle file upload if provided
    if file and file.filename:
        # Delete old file if exists
        if db_item.file_path:
            old_file_path = f"uploads/{db_item.file_path}"
            if os.path.exists(old_file_path):
                try:
                    os.remove(old_file_path)
                    logger.info(f"✅ Deleted old file: {old_file_path}")
                except Exception as e:
                    logger.error(f"⚠️ Could not delete old file: {e}")
        
        # Save new file
        new_file_path = save_upload(file)
        db_item.file_path = new_file_path
    
    db_item.updated_at = datetime.utcnow()
    
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    
    logger.info(f"✅ Item updated with file: {db_item.id} by user {user.email}")
    return db_item


@router.delete("/items/{item_id}")
@router.delete("/items/{item_id}/")
@limiter.limit("20/minute")
async def delete_item(
    request: Request,
    item_id: int,
    session: Session = Depends(get_session),
    user: User = Depends(require_verified_email)
):
    """
    Delete an item and its associated file
    """
    item = session.get(Item, item_id)
    
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    if item.user_id != user.id:
        logger.warning(f"⚠️ User {user.email} attempted to delete item {item_id} owned by another user")
        raise HTTPException(status_code=403, detail="Not authorized to delete this item")

    # Delete associated file if exists
    if item.file_path:
        file_path = f"uploads/{item.file_path}"
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                logger.info(f"✅ Deleted file: {file_path}")
            except Exception as e:
                logger.error(f"⚠️ Could not delete file: {e}")

    session.delete(item)
    session.commit()
    
    logger.info(f"✅ Item deleted: {item_id} by user {user.email}")
    return {"message": "Item deleted successfully", "id": item_id}


@router.post("/items/upload")
@router.post("/items/upload/")
@limiter.limit("20/minute")
async def upload_item(
    request: Request,
    name: str = Form(...),
    category: str = Form(...),
    type: str = Form(...),

    expiration_date: Optional[str] = Form(None),
    renewal_date: Optional[str] = Form(None),
    billing_cycle: Optional[str] = Form(None),
    price: Optional[float] = Form(None),

    document_number: Optional[str] = Form(None),
    notes: Optional[str] = Form(None),
    reminder_days_before: Optional[int] = Form(None),
    
    # New fields for dynamic support
    item_type_id: Optional[int] = Form(None),
    item_type_name: Optional[str] = Form(None),
    dynamic_fields: Optional[str] = Form(None),  # JSON string
    
    file: UploadFile = File(None),

    session: Session = Depends(get_session),
    user: User = Depends(require_verified_email)
):
    """
    Create a new item with file upload.
    Supports both legacy fields and new dynamic_fields JSON.
    """
    
    # Check item count limit for free users
    from sqlmodel import select, func
    statement = select(func.count(Item.id)).where(Item.user_id == user.id)
    item_count = session.exec(statement).one()
    
    if not user.can_add_items(item_count):
        logger.warning(f"⚠️ Free user {user.email} attempted to exceed 20 item limit")
        raise HTTPException(
            status_code=403,
            detail="Free plan limited to 20 items. Upgrade to Premium for unlimited items."
        )
    
    # Validate input
    if len(name) > 200:
        raise HTTPException(status_code=400, detail="Name must not exceed 200 characters")
    
    validate_item_fields(name, type, category)
    
    # Validate file if provided
    if file and file.filename:
        is_valid, error_msg = validate_file(file)
        if not is_valid:
            raise HTTPException(status_code=400, detail=error_msg)
    
    # Validate dynamic_fields JSON if provided
    if dynamic_fields:
        try:
            json.loads(dynamic_fields)
        except (json.JSONDecodeError, ValueError):
            raise HTTPException(status_code=400, detail="Invalid JSON format for dynamic_fields")
    
    # Parse dates
    expiration_date_parsed = parse_date(expiration_date)
    renewal_date_parsed = parse_date(renewal_date)
    
    # Save file
    file_path = save_upload(file) if file else None

    # Create item
    item = Item(
        name=name.strip(),
        category=category,
        type=type,
        item_type_id=item_type_id,
        item_type_name=item_type_name,
        expiration_date=expiration_date_parsed,
        renewal_date=renewal_date_parsed,
        billing_cycle=billing_cycle if billing_cycle else None,
        price=price if price else None,
        document_number=document_number.strip() if document_number else None,
        notes=notes.strip() if notes else None,
        file_path=file_path,
        reminder_days_before=reminder_days_before,
        dynamic_fields=dynamic_fields if dynamic_fields else "{}",
        user_id=user.id
    )

    session.add(item)
    session.commit()
    session.refresh(item)
    
    logger.info(f"✅ Item uploaded: {item.id} by user {user.email}")
    return item


@router.delete("/items/bulk")
@router.delete("/items/bulk/")
@limiter.limit("10/minute")
async def bulk_delete_items(
    request: Request,
    item_ids: list[int],
    session: Session = Depends(get_session),
    user: User = Depends(require_verified_email)
):
    """
    Delete multiple items at once
    """
    if not item_ids:
        raise HTTPException(status_code=400, detail="No items specified")
    
    if len(item_ids) > 100:
        raise HTTPException(status_code=400, detail="Cannot delete more than 100 items at once")
    
    deleted_count = 0
    files_deleted = 0
    
    for item_id in item_ids:
        item = session.get(Item, item_id)
        
        if not item:
            continue
        
        if item.user_id != user.id:
            logger.warning(f"⚠️ User {user.email} attempted to delete item {item_id} owned by another user")
            continue
        
        # Delete file if exists
        if item.file_path:
            file_path = f"uploads/{item.file_path}"
            if os.path.exists(file_path):
                try:
                    os.remove(file_path)
                    files_deleted += 1
                except Exception as e:
                    logger.error(f"⚠️ Could not delete file: {e}")
        
        session.delete(item)
        deleted_count += 1
    
    session.commit()
    
    logger.info(f"✅ Bulk deleted {deleted_count} items by user {user.email}")
    
    return {
        "message": f"Successfully deleted {deleted_count} items",
        "deleted_count": deleted_count,
        "files_deleted": files_deleted
    }
