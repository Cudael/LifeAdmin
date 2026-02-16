import sqlite3

def migrate():
    """Add subscription columns to user table"""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # List of columns to add with their defaults
    columns = [
        ("stripe_customer_id", "TEXT", None),
        ("stripe_subscription_id", "TEXT", None),
        ("subscription_status", "TEXT", None),
        ("subscription_plan", "TEXT", "free"),
        ("subscription_current_period_end", "TIMESTAMP", None)
    ]
    
    # Note: SQLite ALTER TABLE doesn't support parameterized queries for column definitions
    # However, since we're using controlled, hardcoded column names and types (not user input),
    # this is safe. We validate the column names to prevent any injection attempts.
    allowed_columns = {"stripe_customer_id", "stripe_subscription_id", "subscription_status", "subscription_plan", "subscription_current_period_end"}
    allowed_types = {"TEXT", "TIMESTAMP"}
    
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
                # For TEXT with default value
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
    
    # Set subscription_plan to 'free' for all existing users who don't have it set
    try:
        cursor.execute("UPDATE user SET subscription_plan = 'free' WHERE subscription_plan IS NULL")
        conn.commit()
        rows_updated = cursor.rowcount
        print(f"✅ Set subscription_plan to 'free' for {rows_updated} existing users")
    except Exception as e:
        print(f"⚠️ Could not update subscription plans: {e}")
    
    # Create index on stripe_customer_id for faster lookups
    try:
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_user_stripe_customer_id ON user(stripe_customer_id)")
        print("✅ Created index on stripe_customer_id")
    except Exception as e:
        print(f"⚠️ Could not create index: {e}")
    
    conn.close()
    print("\n🎉 Migration complete!")

if __name__ == "__main__":
    migrate()
