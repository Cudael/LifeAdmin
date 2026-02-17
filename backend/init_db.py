#!/usr/bin/env python3
"""
Database Initialization Script

This script initializes the database with the correct schema.
It creates all tables from all models including:
- User (with all auth, OAuth, notification, display, subscription fields)
- Item (with dynamic fields support)
- ItemType (for managing item templates)
- Notification (for user notifications)

Usage:
    python init_db.py

This will:
1. Delete the existing database.db if it exists
2. Create a fresh database.db with all tables
3. Print confirmation of tables created
"""

import os
import sys
import logging
from pathlib import Path

# Add the backend directory to the Python path
backend_dir = Path(__file__).parent
sys.path.insert(0, str(backend_dir))

from sqlmodel import SQLModel, create_engine
from database import DATABASE_URL, engine

# Import all models so SQLModel can create their tables
from models.user import User
from models.item import Item
from models.item_type import ItemType
from models.notification import Notification

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def init_database():
    """Initialize the database with all tables"""
    
    # Get database file path from DATABASE_URL
    db_file = DATABASE_URL.replace("sqlite:///", "")
    db_path = backend_dir / db_file
    
    logger.info("=" * 60)
    logger.info("Database Initialization Script")
    logger.info("=" * 60)
    
    # Delete existing database if it exists
    if db_path.exists():
        logger.warning(f"Existing database found at: {db_path}")
        response = input("Delete existing database and create fresh one? (yes/no): ")
        if response.lower() in ['yes', 'y']:
            db_path.unlink()
            logger.info(f"✅ Deleted existing database: {db_path}")
        else:
            logger.info("Cancelled. Exiting without changes.")
            return
    
    # Create all tables
    logger.info(f"Creating database at: {db_path}")
    logger.info("Creating tables...")
    
    try:
        SQLModel.metadata.create_all(engine)
        logger.info("✅ All tables created successfully!")
        
        # List all tables created
        logger.info("\nTables created:")
        for table_name in SQLModel.metadata.tables.keys():
            logger.info(f"  - {table_name}")
        
        logger.info("\n" + "=" * 60)
        logger.info("Database initialization complete!")
        logger.info("=" * 60)
        logger.info(f"\nDatabase location: {db_path}")
        logger.info("\nYou can now run the backend server:")
        logger.info("  uvicorn main:app --reload --host 0.0.0.0 --port 8000")
        
    except Exception as e:
        logger.error(f"❌ Error creating database: {e}")
        logger.exception("Detailed error:")
        sys.exit(1)


if __name__ == "__main__":
    init_database()
