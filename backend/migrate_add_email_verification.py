import sqlite3
from datetime import datetime

def migrate():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    print("🔧 Adding email verification fields to user table...")
    
    try:
        # Add email_verified column
        cursor.execute("""
            ALTER TABLE user 
            ADD COLUMN email_verified BOOLEAN DEFAULT 0
        """)
        print("✅ Added email_verified column")
        
        # Add email_verified_at column
        cursor.execute("""
            ALTER TABLE user 
            ADD COLUMN email_verified_at DATETIME
        """)
        print("✅ Added email_verified_at column")
        
        # Create email_verification_tokens table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS email_verification_tokens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                token TEXT NOT NULL UNIQUE,
                expires_at DATETIME NOT NULL,
                used BOOLEAN DEFAULT 0,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
            )
        """)
        print("✅ Created email_verification_tokens table")
        
        # Create indexes
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_verification_token 
            ON email_verification_tokens(token)
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_verification_user_id 
            ON email_verification_tokens(user_id)
        """)
        print("✅ Created indexes")
        
        # Set existing users as verified (grandfather them in)
        cursor.execute("""
            UPDATE user 
            SET email_verified = 1, email_verified_at = CURRENT_TIMESTAMP
            WHERE email_verified IS NULL OR email_verified = 0
        """)
        verified_count = cursor.rowcount
        print(f"✅ Marked {verified_count} existing users as verified")
        
        conn.commit()
        print("🎉 Migration complete!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    migrate()