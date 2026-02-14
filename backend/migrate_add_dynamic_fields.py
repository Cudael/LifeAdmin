#!/usr/bin/env python3
"""
Migration script to add dynamic fields support to items table and create item_types table.

This adds:
1. item_type_id, item_type_name, and dynamic_fields columns to items table
2. Creates the item_types table
3. Seeds initial item type templates

Run this script to update your database schema:
    python migrate_add_dynamic_fields.py
"""

import sqlite3
import json
from datetime import datetime

DATABASE_PATH = "database.db"


def create_item_types_table(cursor):
    """Create the item_types table"""
    print("Creating item_types table...")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS item_types (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            item_class TEXT NOT NULL,
            description TEXT,
            icon TEXT,
            fields_config TEXT NOT NULL DEFAULT '[]',
            is_active INTEGER NOT NULL DEFAULT 1,
            created_at TEXT NOT NULL,
            updated_at TEXT
        )
    """)
    
    # Create indexes
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_item_types_name ON item_types(name)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_item_types_category ON item_types(category)")
    print("✅ item_types table created")


def add_dynamic_fields_columns(cursor):
    """Add new columns to items table"""
    print("Adding columns to items table...")
    
    # Check if columns already exist
    cursor.execute("PRAGMA table_info(items)")
    columns = [col[1] for col in cursor.fetchall()]
    
    if "item_type_id" not in columns:
        cursor.execute("ALTER TABLE items ADD COLUMN item_type_id INTEGER")
        print("✅ Added item_type_id column")
    else:
        print("⏭️  item_type_id column already exists")
    
    if "item_type_name" not in columns:
        cursor.execute("ALTER TABLE items ADD COLUMN item_type_name TEXT")
        print("✅ Added item_type_name column")
    else:
        print("⏭️  item_type_name column already exists")
    
    if "dynamic_fields" not in columns:
        cursor.execute("ALTER TABLE items ADD COLUMN dynamic_fields TEXT DEFAULT '{}'")
        print("✅ Added dynamic_fields column")
    else:
        print("⏭️  dynamic_fields column already exists")


def seed_item_types(cursor):
    """Seed initial item type templates"""
    print("Seeding item types...")
    
    now = datetime.utcnow().isoformat()
    
    item_types = [
        # Travel Documents
        {
            "name": "Passport",
            "category": "Travel",
            "item_class": "document",
            "description": "Travel passport document",
            "icon": "🛂",
            "fields": [
                {"name": "expiration_date", "label": "Expiration Date", "field_type": "date", "required": True},
                {"name": "document_number", "label": "Passport Number", "field_type": "text", "required": False},
                {"name": "issuing_country", "label": "Issuing Country", "field_type": "text", "required": False},
                {"name": "issue_date", "label": "Issue Date", "field_type": "date", "required": False},
            ]
        },
        {
            "name": "Visa",
            "category": "Travel",
            "item_class": "document",
            "description": "Travel visa",
            "icon": "✈️",
            "fields": [
                {"name": "expiration_date", "label": "Expiration Date", "field_type": "date", "required": True},
                {"name": "visa_type", "label": "Visa Type", "field_type": "text", "required": False},
                {"name": "document_number", "label": "Visa Number", "field_type": "text", "required": False},
                {"name": "country", "label": "Country", "field_type": "text", "required": False},
            ]
        },
        {
            "name": "Driver's License",
            "category": "Vehicle",
            "item_class": "document",
            "description": "Driving license",
            "icon": "🚗",
            "fields": [
                {"name": "expiration_date", "label": "Expiration Date", "field_type": "date", "required": True},
                {"name": "document_number", "label": "License Number", "field_type": "text", "required": False},
                {"name": "license_class", "label": "License Class", "field_type": "text", "required": False},
                {"name": "issuing_state", "label": "Issuing State/Province", "field_type": "text", "required": False},
            ]
        },
        
        # Personal Documents
        {
            "name": "ID Card",
            "category": "Personal",
            "item_class": "document",
            "description": "National identification card",
            "icon": "🪪",
            "fields": [
                {"name": "expiration_date", "label": "Expiration Date", "field_type": "date", "required": True},
                {"name": "document_number", "label": "ID Number", "field_type": "text", "required": False},
                {"name": "issuing_authority", "label": "Issuing Authority", "field_type": "text", "required": False},
            ]
        },
        
        # Health Documents
        {
            "name": "Health Insurance Card",
            "category": "Health",
            "item_class": "document",
            "description": "Health insurance coverage card",
            "icon": "🏥",
            "fields": [
                {"name": "expiration_date", "label": "Expiration Date", "field_type": "date", "required": True},
                {"name": "policy_number", "label": "Policy Number", "field_type": "text", "required": False},
                {"name": "provider", "label": "Insurance Provider", "field_type": "text", "required": False},
                {"name": "group_number", "label": "Group Number", "field_type": "text", "required": False},
            ]
        },
        
        # Legal Documents
        {
            "name": "Warranty",
            "category": "Legal",
            "item_class": "document",
            "description": "Product warranty",
            "icon": "🔧",
            "fields": [
                {"name": "expiration_date", "label": "Warranty Expiration", "field_type": "date", "required": True},
                {"name": "product_name", "label": "Product Name", "field_type": "text", "required": False},
                {"name": "serial_number", "label": "Serial Number", "field_type": "text", "required": False},
                {"name": "purchase_date", "label": "Purchase Date", "field_type": "date", "required": False},
                {"name": "retailer", "label": "Retailer", "field_type": "text", "required": False},
            ]
        },
        
        # Subscriptions
        {
            "name": "Netflix Subscription",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Netflix streaming subscription",
            "icon": "🎬",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Monthly Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False, 
                 "options": ["Monthly", "Quarterly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "text", "required": False},
            ]
        },
        {
            "name": "Spotify Subscription",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Spotify music subscription",
            "icon": "🎵",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Monthly Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "text", "required": False},
            ]
        },
        {
            "name": "Gym Membership",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Fitness gym membership",
            "icon": "💪",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Monthly Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Quarterly", "Yearly"]},
                {"name": "membership_id", "label": "Membership ID", "field_type": "text", "required": False},
                {"name": "gym_location", "label": "Gym Location", "field_type": "text", "required": False},
            ]
        },
        
        # Generic types for flexibility
        {
            "name": "Generic Document",
            "category": "Personal",
            "item_class": "document",
            "description": "Generic document type",
            "icon": "📄",
            "fields": [
                {"name": "expiration_date", "label": "Expiration Date", "field_type": "date", "required": False},
                {"name": "document_number", "label": "Document Number", "field_type": "text", "required": False},
            ]
        },
        {
            "name": "Generic Subscription",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Generic subscription type",
            "icon": "🔄",
            "fields": [
                {"name": "renewal_date", "label": "Renewal Date", "field_type": "date", "required": False},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Quarterly", "Yearly"]},
            ]
        },
    ]
    
    for item_type in item_types:
        # Check if this type already exists
        cursor.execute("SELECT id FROM item_types WHERE name = ? AND category = ?", 
                      (item_type["name"], item_type["category"]))
        if cursor.fetchone():
            print(f"⏭️  Item type '{item_type['name']}' already exists")
            continue
        
        fields_json = json.dumps(item_type["fields"])
        cursor.execute("""
            INSERT INTO item_types (name, category, item_class, description, icon, fields_config, is_active, created_at)
            VALUES (?, ?, ?, ?, ?, ?, 1, ?)
        """, (
            item_type["name"],
            item_type["category"],
            item_type["item_class"],
            item_type["description"],
            item_type["icon"],
            fields_json,
            now
        ))
        print(f"✅ Created item type: {item_type['name']}")
    
    print(f"✅ Seeded {len(item_types)} item types")


def main():
    """Run the migration"""
    print("=" * 60)
    print("MIGRATION: Add Dynamic Fields Support")
    print("=" * 60)
    
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        
        # Create item_types table
        create_item_types_table(cursor)
        
        # Add columns to items table
        add_dynamic_fields_columns(cursor)
        
        # Seed item types
        seed_item_types(cursor)
        
        conn.commit()
        print("\n" + "=" * 60)
        print("✅ Migration completed successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Migration failed: {e}")
        import traceback
        traceback.print_exc()
        conn.rollback()
        return 1
    
    finally:
        conn.close()
    
    return 0


if __name__ == "__main__":
    exit(main())
