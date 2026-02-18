from fastapi import HTTPException

ALLOWED_CATEGORIES = [
    "Travel", "Health", "Finance", "Work", "Personal",
    "Subscriptions", "Legal", "Education", "Vehicle"
]
ALLOWED_ITEM_TYPES = ["document", "subscription"]

def validate_item_fields(name: str, item_type: str, category: str) -> None:
    """Validate item fields, raising HTTPException on failure."""
    if not name or not name.strip():
        raise HTTPException(status_code=422, detail="Item name cannot be empty.")
    if item_type not in ALLOWED_ITEM_TYPES:
        raise HTTPException(
            status_code=422,
            detail=f"Invalid type '{item_type}'. Must be one of: {ALLOWED_ITEM_TYPES}"
        )
    if category not in ALLOWED_CATEGORIES:
        raise HTTPException(
            status_code=422,
            detail=f"Invalid category '{category}'. Must be one of: {ALLOWED_CATEGORIES}"
        )
