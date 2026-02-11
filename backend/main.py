# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from starlette.middleware.sessions import SessionMiddleware  # ✅ NEW
import os
from dotenv import load_dotenv

from database import create_db_and_tables
from routes.auth import router as auth_router
from routes.items import router as items_router
from routes.oauth import router as oauth_router  # ✅ NEW
from routes.notifications import router as notifications_router  # ADD THIS

load_dotenv()

app = FastAPI(title="DocVault API")

# Serve uploaded files
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

FRONTEND_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=FRONTEND_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Session Middleware (required for OAuth)
app.add_middleware(
    SessionMiddleware, 
    secret_key=os.getenv("SECRET_KEY", "your-secret-key-change-this")
)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Health check
@app.get("/")
def read_root():
    return {"message": "DocVault API is running", "status": "ok"}

# Register routes
app.include_router(auth_router)
app.include_router(items_router)
app.include_router(oauth_router)  # ✅ NEW
app.include_router(notifications_router)  # ✅ NEW