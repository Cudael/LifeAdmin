# Backend Routes Structure

This document describes the modular route structure of the Remindes API.

## Overview

All routes have been split into modular, maintainable structures for future-proofing and scalability.

## Route Modules

### Auth Routes (`/auth`)
**Location:** `routes/auth/`

Handles all authentication and user management endpoints.

**Modules:**
- `registration.py` - User registration
- `login.py` - Login and token refresh
- `password.py` - Password change, forgot, reset
- `verification.py` - Email verification
- `profile.py` - User profile management
- `settings.py` - User preferences and settings
- `oauth.py` - Google OAuth integration

**Shared modules:**
- `_schemas.py` - Pydantic models
- `_validation.py` - Password validation
- `_email.py` - Email sending functions

**Endpoints:** 18 total

### Items Routes (`/items`)
**Location:** `routes/items/`

Manages user items (documents and subscriptions).

**Modules:**
- `crud.py` - Create, read, update, delete operations
- `search.py` - List and search with filters
- `stats.py` - Statistics and analytics

**Endpoints:** 9 total

### Notifications Routes (`/notifications`)
**Location:** `routes/notifications/`

Handles user notifications and reminders.

**Modules:**
- `list.py` - Get notifications with pagination
- `crud.py` - Mark read, delete notifications

**Endpoints:** 6 total

### Item Types Routes (`/item-types`)
**Location:** `routes/item_types/`

Manages item type definitions.

**Modules:**
- `crud.py` - CRUD operations for item types

**Endpoints:** 3 total

## Import Pattern

All route modules follow the same pattern:

```python
# In main.py
from routes.auth import router as auth_router
from routes.items import router as items_router
# etc.

app.include_router(auth_router)
app.include_router(items_router)
# etc.
```

Each module directory has an `__init__.py` that:
1. Imports all sub-routers
2. Creates a main router with the prefix
3. Includes all sub-routers
4. Exports the main router

## Adding New Endpoints

To add a new endpoint to an existing module:

1. Open the appropriate sub-module file
2. Add your endpoint using the module's router
3. No changes needed to `__init__.py` or `main.py`

Example:
```python
# In routes/auth/profile.py
@router.get("/avatar")
def get_avatar(user: User = Depends(get_current_user)):
    return {"avatar": user.profile_picture}
```

## Creating New Route Modules

To create a new top-level route module:

1. Create a directory: `routes/your_module/`
2. Create sub-module files: `crud.py`, `list.py`, etc.
3. Create `__init__.py`:
```python
from fastapi import APIRouter
from .crud import router as crud_router
# Import other sub-routers

router = APIRouter(prefix="/your-prefix", tags=["your-tag"])
router.include_router(crud_router)
# Include other sub-routers
```
4. Update `main.py` to import and include your router

## Benefits of This Structure

✅ **Maintainability** - Small, focused files (all under 500 lines)
✅ **Scalability** - Easy to add new endpoints or modules
✅ **Testability** - Each module can be tested independently
✅ **Readability** - Clear organization and separation of concerns
✅ **Future-proof** - Room to grow without creating monolithic files

## Total Endpoints

**36 API endpoints** across 4 main route modules.
