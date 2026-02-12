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
    
    # Note: SQLite ALTER TABLE doesn't support parameterized queries for column definitions
    # However, since we're using controlled, hardcoded column names and types (not user input),
    # this is safe. We validate the column names to prevent any injection attempts.
    allowed_columns = {"date_format", "time_format", "items_per_page", "default_sort", "language", "timezone", "updated_at"}
    allowed_types = {"TEXT", "INTEGER", "TIMESTAMP"}
    
    for col_name, col_type, default_value in columns:
        # Security: Validate column name and type against whitelist
        if col_name not in allowed_columns:
            print(f"⚠️ Skipping invalid column name: {col_name}")
            continue
        if col_type not in allowed_types:
            print(f"⚠️ Skipping invalid column type for {col_name}: {col_type}")
            continue
            
        try:
            if default_value:
                if col_type == "INTEGER":
                    # Validate that default_value is actually an integer
                    try:
                        int(default_value)
                        cursor.execute(f"ALTER TABLE user ADD COLUMN {col_name} {col_type} DEFAULT {default_value}")
                    except ValueError:
                        print(f"⚠️ Invalid integer default for {col_name}: {default_value}")
                        continue
                else:
                    # For TEXT/TIMESTAMP, escape single quotes in default value
                    safe_default = default_value.replace("'", "''")
                    cursor.execute(f"ALTER TABLE user ADD COLUMN {col_name} {col_type} DEFAULT '{safe_default}'")
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