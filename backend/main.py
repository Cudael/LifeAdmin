# backend/main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from starlette.middleware.sessions import SessionMiddleware
import os
import logging
from dotenv import load_dotenv

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

from database import create_db_and_tables
from routes.auth import router as auth_router
from routes.items import router as items_router
from routes.notifications import router as notifications_router
from routes.item_types import router as item_types_router
from routes.payments import router as payments_router
from routes.contact import router as contact_router

load_dotenv()

# ✅ Setup logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        RotatingFileHandler('app.log', maxBytes=10_000_000, backupCount=5),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ✅ Initialize rate limiter
limiter = Limiter(key_func=get_remote_address)

app = FastAPI(
    title="Remindes API",
    description="Document and subscription management system",
    version="1.0.0"
)

# ✅ Add rate limiter to app state
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# ✅ Serve uploaded files
os.makedirs("uploads", exist_ok=True)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# ✅ CORS Configuration (with production support)
FRONTEND_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    os.getenv("FRONTEND_URL", ""),  # Production frontend URL from .env
]

# Remove empty strings
FRONTEND_ORIGINS = [origin for origin in FRONTEND_ORIGINS if origin]

app.add_middleware(
    CORSMiddleware,
    allow_origins=FRONTEND_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Session Middleware (required for OAuth)
# Import SECRET_KEY from auth utils (already validated there)
from utils.auth import SECRET_KEY

app.add_middleware(
    SessionMiddleware, 
    secret_key=SECRET_KEY,
    max_age=3600,  # 1 hour
    same_site="lax",
    https_only=os.getenv("SECURE_COOKIES", "false").lower() == "true"
)


# ✅ File upload size limit middleware (10MB)
@app.middleware("http")
async def limit_upload_size(request: Request, call_next):
    """Limit file upload size to 10MB"""
    if request.method == "POST":
        content_type = request.headers.get("content-type", "")
        if "multipart/form-data" in content_type:
            content_length = request.headers.get("content-length")
            if content_length and int(content_length) > 10 * 1024 * 1024:  # 10MB
                logger.warning(f"File upload too large: {content_length} bytes from {request.client.host}")
                return JSONResponse(
                    status_code=413,
                    content={"detail": "File too large. Maximum size is 10MB."}
                )
    
    response = await call_next(request)
    return response


# ✅ Security headers middleware
@app.middleware("http")
async def add_security_headers(request: Request, call_next):
    """Add security headers to all responses"""
    response = await call_next(request)
    
    # Prevent MIME type sniffing
    response.headers["X-Content-Type-Options"] = "nosniff"
    
    # Prevent clickjacking
    response.headers["X-Frame-Options"] = "DENY"
    
    # Enable XSS filter in older browsers
    response.headers["X-XSS-Protection"] = "1; mode=block"
    
    # Referrer policy
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    
    # Permissions policy
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    
    # HSTS for production (only if HTTPS is enabled)
    if os.getenv("SECURE_COOKIES", "false").lower() == "true":
        response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    
    return response


# ✅ Request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all requests and responses"""
    logger.info(f"Request: {request.method} {request.url.path} from {request.client.host}")
    
    try:
        response = await call_next(request)
        logger.info(f"Response: {response.status_code} for {request.method} {request.url.path}")
        return response
    except Exception as e:
        logger.error(f"Error processing request {request.method} {request.url.path}: {str(e)}")
        raise


# ✅ Startup event
@app.on_event("startup")
async def startup_event():
    """Initialize database and log startup"""
    logger.info("🚀 Remindes API starting up...")
    create_db_and_tables()
    logger.info(f"✅ Database initialized")
    logger.info(f"✅ CORS enabled for: {', '.join(FRONTEND_ORIGINS)}")
    logger.info(f"✅ File uploads: 10MB limit")
    logger.info(f"✅ Rate limiting: Enabled")
    logger.info("🎉 Remindes API ready!")


# ✅ Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """Log shutdown"""
    logger.info("👋 Remindes API shutting down...")


# ✅ Health check endpoint
@app.get("/", tags=["Health"])
def read_root():
    """Health check endpoint"""
    return {
        "message": "Remindes API is running",
        "status": "ok",
        "version": "1.0.0"
    }


# ✅ Detailed health check
@app.get("/health", tags=["Health"])
def health_check():
    """Detailed health check with system status"""
    import sqlite3
    
    db_status = "ok"
    try:
        conn = sqlite3.connect('database.db')
        conn.close()
    except Exception as e:
        db_status = f"error: {str(e)}"
        logger.error(f"Database health check failed: {e}")
    
    uploads_status = "ok" if os.path.exists("uploads") else "error: uploads directory missing"
    
    return {
        "status": "healthy" if db_status == "ok" else "degraded",
        "database": db_status,
        "uploads": uploads_status,
        "version": "1.0.0"
    }


# ✅ Register routes
app.include_router(auth_router)
app.include_router(items_router)
app.include_router(item_types_router)
app.include_router(notifications_router)
app.include_router(payments_router)
app.include_router(contact_router)


# ✅ Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    """Catch all unhandled exceptions"""
    logger.error(f"Unhandled exception: {str(exc)}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "detail": "An internal server error occurred. Please try again later."
        }
    )