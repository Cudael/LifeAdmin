#!/usr/bin/env python3
"""
Migration script to add more popular subscription types to the item_types table.

Run this script to update your database:
    python migrations/007_add_more_subscriptions.py
"""

import sqlite3
import json
from datetime import datetime

DATABASE_PATH = "database.db"


def seed_more_subscriptions(cursor):
    """Seed additional popular subscription item types"""
    print("Seeding additional subscription types...")

    now = datetime.utcnow().isoformat()

    item_types = [
        # Streaming / Video
        {
            "name": "YouTube Premium",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "YouTube ad-free streaming subscription",
            "icon": "🎥",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Individual", "Family", "Student"]},
            ]
        },
        {
            "name": "Disney+",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Disney+ streaming subscription",
            "icon": "🏰",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Basic", "Standard", "Premium"]},
            ]
        },
        {
            "name": "HBO Max",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "HBO Max streaming subscription",
            "icon": "🎬",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Ad-Lite", "Ad-Free", "Ultimate"]},
            ]
        },
        {
            "name": "Amazon Prime",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Amazon Prime membership (streaming + shopping benefits)",
            "icon": "📦",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "text", "required": False},
            ]
        },
        {
            "name": "Apple TV+",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Apple TV+ streaming subscription",
            "icon": "🍎",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "text", "required": False},
            ]
        },
        {
            "name": "Hulu",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Hulu streaming subscription",
            "icon": "📺",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["With Ads", "No Ads", "Live TV"]},
            ]
        },
        {
            "name": "Paramount+",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Paramount+ streaming subscription",
            "icon": "⭐",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Essential", "Premium"]},
            ]
        },
        {
            "name": "Crunchyroll",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Crunchyroll anime streaming subscription",
            "icon": "🍥",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Fan", "Mega Fan", "Ultimate Fan"]},
            ]
        },
        {
            "name": "Twitch",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Twitch channel subscription",
            "icon": "🎮",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly"]},
                {"name": "channel_name", "label": "Channel Name", "field_type": "text", "required": False},
                {"name": "plan_type", "label": "Tier", "field_type": "select", "required": False,
                 "options": ["Tier 1", "Tier 2", "Tier 3"]},
            ]
        },

        # Music
        {
            "name": "Apple Music",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Apple Music streaming subscription",
            "icon": "🎵",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Individual", "Family", "Student", "Voice"]},
            ]
        },
        {
            "name": "Tidal",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Tidal HiFi music streaming subscription",
            "icon": "🌊",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["HiFi", "HiFi Plus"]},
            ]
        },
        {
            "name": "YouTube Music",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "YouTube Music streaming subscription",
            "icon": "🎶",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Individual", "Family", "Student"]},
            ]
        },

        # Cloud / Productivity
        {
            "name": "Google One",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Google One cloud storage subscription",
            "icon": "☁️",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "storage_size", "label": "Storage Size (GB)", "field_type": "number", "required": False},
            ]
        },
        {
            "name": "iCloud+",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Apple iCloud+ storage subscription",
            "icon": "🍏",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "storage_size", "label": "Storage Size (GB)", "field_type": "number", "required": False},
            ]
        },
        {
            "name": "Notion",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Notion notes and productivity subscription",
            "icon": "📝",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Plus", "Business", "Enterprise"]},
                {"name": "seats", "label": "Number of Seats", "field_type": "number", "required": False},
            ]
        },
        {
            "name": "Slack",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Slack team communication subscription",
            "icon": "💬",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Pro", "Business+", "Enterprise Grid"]},
                {"name": "seats", "label": "Number of Seats", "field_type": "number", "required": False},
            ]
        },
        {
            "name": "Zoom",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Zoom video conferencing subscription",
            "icon": "📹",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Pro", "Business", "Business Plus", "Enterprise"]},
                {"name": "seats", "label": "Number of Seats", "field_type": "number", "required": False},
            ]
        },

        # Gaming
        {
            "name": "PlayStation Plus",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "PlayStation Plus online gaming subscription",
            "icon": "🎮",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Essential", "Extra", "Premium"]},
                {"name": "games_included", "label": "Games Included", "field_type": "textarea", "required": False},
            ]
        },
        {
            "name": "Xbox Game Pass",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Xbox Game Pass subscription",
            "icon": "🎯",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Core", "PC Game Pass", "Ultimate"]},
                {"name": "games_included", "label": "Games Included", "field_type": "textarea", "required": False},
            ]
        },
        {
            "name": "Nintendo Switch Online",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Nintendo Switch Online gaming subscription",
            "icon": "🕹️",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Individual", "Family", "Expansion Pack"]},
                {"name": "games_included", "label": "Games Included", "field_type": "textarea", "required": False},
            ]
        },
        {
            "name": "Steam",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Steam game subscription (e.g., EA Play on Steam, game-specific subscriptions)",
            "icon": "🎲",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "text", "required": False},
                {"name": "games_included", "label": "Games Included", "field_type": "textarea", "required": False},
            ]
        },

        # Other Popular
        {
            "name": "ChatGPT Plus",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "ChatGPT Plus AI assistant subscription",
            "icon": "🤖",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Plus", "Team", "Enterprise"]},
            ]
        },
        {
            "name": "NordVPN",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "NordVPN virtual private network subscription",
            "icon": "🔒",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly", "2 Years"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Standard", "Plus", "Complete"]},
                {"name": "data_allowance", "label": "Data Allowance", "field_type": "text", "required": False},
            ]
        },
        {
            "name": "ExpressVPN",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "ExpressVPN virtual private network subscription",
            "icon": "🛡️",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "6 Months", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "text", "required": False},
                {"name": "data_allowance", "label": "Data Allowance", "field_type": "text", "required": False},
            ]
        },
        {
            "name": "Duolingo",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Duolingo language learning subscription",
            "icon": "🦉",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Super", "Max", "Family"]},
                {"name": "language", "label": "Learning Language", "field_type": "text", "required": False},
            ]
        },
        {
            "name": "Audible",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Audible audiobook subscription",
            "icon": "🎧",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "select", "required": False,
                 "options": ["Plus", "Premium Plus"]},
                {"name": "credits_per_month", "label": "Credits Per Month", "field_type": "number", "required": False},
            ]
        },
        {
            "name": "Kindle Unlimited",
            "category": "Subscriptions",
            "item_class": "subscription",
            "description": "Kindle Unlimited ebook subscription",
            "icon": "📚",
            "fields": [
                {"name": "renewal_date", "label": "Next Renewal Date", "field_type": "date", "required": True},
                {"name": "price", "label": "Price", "field_type": "number", "required": False},
                {"name": "billing_cycle", "label": "Billing Cycle", "field_type": "select", "required": False,
                 "options": ["Monthly", "Yearly"]},
                {"name": "plan_type", "label": "Plan Type", "field_type": "text", "required": False},
            ]
        },
    ]

    for item_type in item_types:
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

    print(f"✅ Processed {len(item_types)} additional subscription types")


def main():
    """Run the migration"""
    print("=" * 60)
    print("MIGRATION 007: Add More Popular Subscription Types")
    print("=" * 60)

    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()

        seed_more_subscriptions(cursor)

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
