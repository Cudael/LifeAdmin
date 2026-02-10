from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from database import create_db_and_tables
from routes.auth import router as auth_router
from routes.items import router as items_router

app = FastAPI()

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

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Register routes
app.include_router(auth_router)
app.include_router(items_router)