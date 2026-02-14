# models/item_type.py
from sqlmodel import SQLModel, Field
from typing import Optional, List
from datetime import datetime
import json


class FieldDefinition(SQLModel):
    """Definition for a single field in an item type"""
    name: str  # Internal field name (e.g., "expiration_date")
    label: str  # Display label (e.g., "Expiration Date")
    field_type: str  # "text", "date", "number", "textarea", "select"
    required: bool = False
    placeholder: Optional[str] = None
    options: Optional[List[str]] = None  # For select fields
    validation: Optional[str] = None  # Validation rules (e.g., "email", "url")


class ItemTypeBase(SQLModel):
    """Base model for item types"""
    name: str = Field(index=True)  # e.g., "Passport", "Netflix Subscription"
    category: str = Field(index=True)  # e.g., "Travel", "Subscriptions"
    item_class: str  # "document" or "subscription"
    description: Optional[str] = None
    icon: Optional[str] = None  # Emoji or icon identifier
    
    # JSON string containing list of FieldDefinition objects
    fields_config: str = Field(default="[]")  # Stored as JSON string
    
    # Whether this type is active and shown to users
    is_active: bool = True


class ItemType(ItemTypeBase, table=True):
    """Database model for item types"""
    __tablename__ = "item_types"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = None
    
    def get_fields(self) -> List[dict]:
        """Parse and return field definitions"""
        try:
            return json.loads(self.fields_config)
        except (json.JSONDecodeError, ValueError) as e:
            import logging
            logging.getLogger(__name__).warning(f"Failed to parse fields_config for item_type {self.id}: {e}")
            return []
    
    def set_fields(self, fields: List[dict]):
        """Set field definitions from list"""
        self.fields_config = json.dumps(fields)


class ItemTypeCreate(ItemTypeBase):
    """Model for creating item types"""
    pass


class ItemTypeRead(ItemTypeBase):
    """Model for reading item types with parsed fields"""
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
