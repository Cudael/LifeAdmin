import sqlite3

def migrate():
    """Add reminder_days_before column to items table"""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # Column to add (optional, defaults to None)
    col_name = "reminder_days_before"
    col_type = "INTEGER"
    
    try:
        # Add the column - NULL by default (falls back to user preference)
        # SECURITY NOTE: Using f-string here is safe because col_name and col_type
        # are hardcoded constants, not user input. SQLite ALTER TABLE does not
        # support parameterized column names/types.
        cursor.execute(f"ALTER TABLE items ADD COLUMN {col_name} {col_type}")
        conn.commit()
        print(f"✅ Added column: {col_name}")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e).lower():
            print(f"⏩ Column {col_name} already exists, skipping")
        else:
            print(f"❌ Error adding {col_name}: {e}")
            raise
    
    conn.close()
    print("\n🎉 Migration complete!")
    print("ℹ️  Existing items will use user's default reminder settings (backward compatible)")

if __name__ == "__main__":
    migrate()
