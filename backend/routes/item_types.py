# backend/routes/item_types.py
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from typing import List, Optional
import json

from models.item_type import ItemType
from models.user import User
from database import get_session
from utils.auth import get_current_user

router = APIRouter(prefix="/item-types", tags=["Item Types"])


@router.get("")
def list_item_types(
    category: Optional[str] = None,
    item_class: Optional[str] = None,  # "document" or "subscription"
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    """
    List all available item types with their field configurations.
    Can be filtered by category or item_class.
    """
    query = select(ItemType).where(ItemType.is_active == True)
    
    if category:
        query = query.where(ItemType.category == category)
    
    if item_class:
        query = query.where(ItemType.item_class == item_class)
    
    query = query.order_by(ItemType.category, ItemType.name)
    
    item_types = session.exec(query).all()
    
    # Parse fields_config JSON for each type
    result = []
    for item_type in item_types:
        item_dict = {
            "id": item_type.id,
            "name": item_type.name,
            "category": item_type.category,
            "item_class": item_type.item_class,
            "description": item_type.description,
            "icon": item_type.icon,
            "fields": item_type.get_fields(),
            "is_active": item_type.is_active,
            "created_at": item_type.created_at.isoformat() if item_type.created_at else None
        }
        result.append(item_dict)
    
    return {"item_types": result, "total": len(result)}


@router.get("/{item_type_id}")
def get_item_type(
    item_type_id: int,
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    """
    Get a specific item type by ID with its field configuration.
    """
    item_type = session.get(ItemType, item_type_id)
    
    if not item_type:
        raise HTTPException(status_code=404, detail="Item type not found")
    
    return {
        "id": item_type.id,
        "name": item_type.name,
        "category": item_type.category,
        "item_class": item_type.item_class,
        "description": item_type.description,
        "icon": item_type.icon,
        "fields": item_type.get_fields(),
        "is_active": item_type.is_active,
        "created_at": item_type.created_at.isoformat() if item_type.created_at else None
    }


@router.get("/categories")
def get_categories(
    session: Session = Depends(get_session),
    user: User = Depends(get_current_user)
):
    """
    Get list of all available categories with count of types in each.
    """
    query = select(ItemType.category, ItemType.item_class).where(ItemType.is_active == True).distinct()
    results = session.exec(query).all()
    
    # Group by category
    categories = {}
    for category, item_class in results:
        if category not in categories:
            categories[category] = {"documents": 0, "subscriptions": 0}
        if item_class == "document":
            categories[category]["documents"] += 1
        elif item_class == "subscription":
            categories[category]["subscriptions"] += 1
    
    return {"categories": categories}
