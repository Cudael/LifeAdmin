"""
Unified authentication router

This module combines all authentication-related routes into a single router.
"""
from fastapi import APIRouter

from .registration import router as registration_router
from .login import router as login_router
from .password import router as password_router
from .verification import router as verification_router
from .profile import router as profile_router
from .settings import router as settings_router
from .oauth import router as oauth_router

# Create the main auth router
router = APIRouter(prefix="/auth", tags=["auth"])

# Include all sub-routers
router.include_router(registration_router)
router.include_router(login_router)
router.include_router(password_router)
router.include_router(verification_router)
router.include_router(profile_router)
router.include_router(settings_router)
router.include_router(oauth_router)
