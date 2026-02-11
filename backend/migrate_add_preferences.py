import sqlite3

def migrate():
    """Add preference columns to user table"""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # List of columns to add with their defaults
    columns = [
        ("date_format", "TEXT", "MM/DD/YYYY"),
        ("time_format", "TEXT", "12h"),
        ("items_per_page", "INTEGER", "25"),
        ("default_sort", "TEXT", "expiration_asc"),
        ("language", "TEXT", "en"),
        ("timezone", "TEXT", "UTC"),
        ("updated_at", "TIMESTAMP", None)
    ]
    
    for col_name, col_type, default_value in columns:
        try:
            if default_value:
                if col_type == "INTEGER":
                    cursor.execute(f"ALTER TABLE user ADD COLUMN {col_name} {col_type} DEFAULT {default_value}")
                else:
                    cursor.execute(f"ALTER TABLE user ADD COLUMN {col_name} {col_type} DEFAULT '{default_value}'")
            else:
                cursor.execute(f"ALTER TABLE user ADD COLUMN {col_name} {col_type}")
            
            print(f"✅ Added column: {col_name}")
        except sqlite3.OperationalError as e:
            if "duplicate column name" in str(e).lower():
                print(f"⏩ Column {col_name} already exists, skipping")
            else:
                print(f"❌ Error adding {col_name}: {e}")
    
    # Set updated_at to created_at for existing users
    try:
        cursor.execute("UPDATE user SET updated_at = created_at WHERE updated_at IS NULL")
        conn.commit()
        print("✅ Set updated_at for existing users")
    except Exception as e:
        print(f"⚠️ Could not update timestamps: {e}")
    
    conn.close()
    print("\n🎉 Migration complete!")

if __name__ == "__main__":
    migrate()