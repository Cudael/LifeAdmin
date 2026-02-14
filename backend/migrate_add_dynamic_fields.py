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
        
        # Software/Cloud Services Subscriptions
        {
            "name": "GitHub Subscription",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "GitHub subscription plan",
            "icon": "💻",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Monthly Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Free", "Pro", "Team", "Enterprise"]},
                {"name": "username", "label": "Username", "field_type": "text", "required": False},
            ]
        },
        {
            "name": "Dropbox Subscription",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Dropbox cloud storage subscription",
            "icon": "☁️",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Monthly Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "storage_size", "label": "Storage Size (GB)", "field_type": "number", "required": False},
                {"name": "plan_type", "label": "Plan Type", "field_type": "text", "required": False},
            ]
        },
        {
            "name": "Adobe Creative Cloud",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Adobe Creative Cloud subscription",
            "icon": "🎨",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Monthly Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Single App", "All Apps", "Photography"]},
                {"name": "apps_included", "label": "Apps Included", "field_type": "textarea", "required": False},
            ]
        },
        {
            "name": "Microsoft 365",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Microsoft 365 subscription",
            "icon": "🖥️",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Monthly Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Personal", "Family", "Business Basic", "Business Standard"]},
                {"name": "seats", "label": "Number of Seats", "field_type": "number", "required": False},
            ]
        },
        
        # Financial Documents
        {
            "name": "Credit Card",
            "category": "Financial",
            "item_class": "document",
            "description": "Credit card information",
            "icon": "💳",
            "fields": [
                {"name": "expiration_date", "label": "Expiration Date", "field_type": "date", "required": True},
                {"name": "card_number_last4", "label": "Last 4 Digits", "field_type": "text", "required": False},
                {"name": "card_holder", "label": "Card Holder Name", "field_type": "text", "required": False},
                {"name": "issuing_bank", "label": "Issuing Bank", "field_type": "text", "required": False},
                {"name": "credit_limit", "label": "Credit Limit", "field_type": "number", "required": False},
            ]
        },
        {
            "name": "Bank Account",
            "category": "Financial",
            "item_class": "document",
            "description": "Bank account information",
            "icon": "🏦",
            "fields": [
                {"name": "account_number", "label": "Account Number", "field_type": "text", "required": False},
                {"name": "bank_name", "label": "Bank Name", "field_type": "text", "required": False},
                {"name": "account_type", "label": "Account Type", "field_type": "select", "required": False,
                 "options": ["Checking", "Savings", "Money Market", "CD"]},
                {"name": "routing_number", "label": "Routing Number", "field_type": "text", "required": False},
            ]
        },
        {
            "name": "Tax Document",
            "category": "Financial",
            "item_class": "document",
            "description": "Tax-related document",
            "icon": "📑",
            "fields": [
                {"name": "tax_year", "label": "Tax Year", "field_type": "number", "required": True},
                {"name": "document_type", "label": "Document Type", "field_type": "select", "required": False,
                 "options": ["W-2", "1099", "1040", "K-1", "Other"]},
                {"name": "filing_date", "label": "Filing Date", "field_type": "date", "required": False},
                {"name": "reference_number", "label": "Reference Number", "field_type": "text", "required": False},
            ]
        },
        
        # Professional Documents
        {
            "name": "Professional Certificate",
            "category": "Professional",
            "item_class": "document",
            "description": "Professional certification",
            "icon": "🎓",
            "fields": [
                {"name": "expiration_date", "label": "Expiration Date", "field_type": "date", "required": False},
                {"name": "certificate_number", "label": "Certificate Number", "field_type": "text", "required": False},
                {"name": "issuing_organization", "label": "Issuing Organization", "field_type": "text", "required": False},
                {"name": "issue_date", "label": "Issue Date", "field_type": "date", "required": False},
                {"name": "certification_name", "label": "Certification Name", "field_type": "text", "required": False},
            ]
        },
        {
            "name": "Professional License",
            "category": "Professional",
            "item_class": "document",
            "description": "Professional license",
            "icon": "📜",
            "fields": [
                {"name": "expiration_date", "label": "Expiration Date", "field_type": "date", "required": True},
                {"name": "license_number", "label": "License Number", "field_type": "text", "required": False},
                {"name": "issuing_authority", "label": "Issuing Authority", "field_type": "text", "required": False},
                {"name": "license_type", "label": "License Type", "field_type": "text", "required": False},
                {"name": "jurisdiction", "label": "Jurisdiction", "field_type": "text", "required": False},
            ]
        },
        {
            "name": "Professional Membership",
            "category": "Professional",
            "item_class": "subscription",
            "description": "Professional organization membership",
            "icon": "👔",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Annual Fee", "field_type": "number", "required": False},
                {"name": "membership_id", "label": "Membership ID", "field_type": "text", "required": False},
                {"name": "organization", "label": "Organization Name", "field_type": "text", "required": False},
                {"name": "membership_level", "label": "Membership Level", "field_type": "text", "required": False},
            ]
        },
        
        # Property/Legal Documents
        {
            "name": "Lease Agreement",
            "category": "Property",
            "item_class": "document",
            "description": "Property lease or rental agreement",
            "icon": "🏠",
            "fields": [
                {"name": "expiration_date", "label": "Lease End Date", "field_type": "date", "required": True},
                {"name": "start_date", "label": "Lease Start Date", "field_type": "date", "required": False},
                {"name": "monthly_rent", "label": "Monthly Rent", "field_type": "number", "required": False},
                {"name": "property_address", "label": "Property Address", "field_type": "textarea", "required": False},
                {"name": "landlord_name", "label": "Landlord Name", "field_type": "text", "required": False},
                {"name": "security_deposit", "label": "Security Deposit", "field_type": "number", "required": False},
            ]
        },
        {
            "name": "Property Deed",
            "category": "Property",
            "item_class": "document",
            "description": "Property ownership deed",
            "icon": "📋",
            "fields": [
                {"name": "property_address", "label": "Property Address", "field_type": "textarea", "required": False},
                {"name": "deed_number", "label": "Deed Number", "field_type": "text", "required": False},
                {"name": "recording_date", "label": "Recording Date", "field_type": "date", "required": False},
                {"name": "parcel_number", "label": "Parcel Number", "field_type": "text", "required": False},
                {"name": "county", "label": "County", "field_type": "text", "required": False},
            ]
        },
        {
            "name": "Legal Contract",
            "category": "Property",
            "item_class": "document",
            "description": "Legal contract or agreement",
            "icon": "📝",
            "fields": [
                {"name": "expiration_date", "label": "Contract End Date", "field_type": "date", "required": False},
                {"name": "start_date", "label": "Contract Start Date", "field_type": "date", "required": False},
                {"name": "contract_type", "label": "Contract Type", "field_type": "text", "required": False},
                {"name": "parties_involved", "label": "Parties Involved", "field_type": "textarea", "required": False},
                {"name": "contract_value", "label": "Contract Value", "field_type": "number", "required": False},
            ]
        },
        
        # Vehicle Documents
        {
            "name": "Vehicle Registration",
            "category": "Vehicle",
            "item_class": "document",
            "description": "Vehicle registration document",
            "icon": "🚙",
            "fields": [
                {"name": "expiration_date", "label": "Expiration Date", "field_type": "date", "required": True},
                {"name": "registration_number", "label": "Registration Number", "field_type": "text", "required": False},
                {"name": "vehicle_make", "label": "Vehicle Make", "field_type": "text", "required": False},
                {"name": "vehicle_model", "label": "Vehicle Model", "field_type": "text", "required": False},
                {"name": "vehicle_year", "label": "Vehicle Year", "field_type": "number", "required": False},
                {"name": "license_plate", "label": "License Plate", "field_type": "text", "required": False},
                {"name": "vin", "label": "VIN", "field_type": "text", "required": False},
            ]
        },
        {
            "name": "Auto Insurance",
            "category": "Vehicle",
            "item_class": "subscription",
            "description": "Auto insurance policy",
            "icon": "🚗",
            "fields": [
                {"name": "renewal_date", "label": "Policy Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Premium Amount", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Semi-Annually", "Annually"]},
                {"name": "policy_number", "label": "Policy Number", "field_type": "text", "required": False},
                {"name": "insurance_company", "label": "Insurance Company", "field_type": "text", "required": False},
                {"name": "coverage_type", "label": "Coverage Type", "field_type": "text", "required": False},
                {"name": "deductible", "label": "Deductible", "field_type": "number", "required": False},
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
