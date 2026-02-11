import sqlite3
from datetime import datetime

def migrate():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    print("🔧 Adding password_reset_tokens table...")
    
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS password_reset_tokens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                token TEXT NOT NULL UNIQUE,
                expires_at DATETIME NOT NULL,
                used BOOLEAN DEFAULT 0,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE
            )
        """)
        
        # Create index for faster lookups
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_reset_token 
            ON password_reset_tokens(token)
        """)
        
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_reset_user_id 
            ON password_reset_tokens(user_id)
        """)
        
        conn.commit()
        print("✅ password_reset_tokens table created successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    migrate()
    print("🎉 Migration complete!")