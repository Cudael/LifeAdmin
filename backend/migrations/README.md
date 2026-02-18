# Database Migrations

This directory contains database migration scripts for the Remindes application.

## Running Migrations

**⚠️ IMPORTANT: Always backup your database before running migrations!**

1. **Backup your database:**
   ```bash
   cp database.db database.db.backup
   ```

2. **Run migrations in order:**
   ```bash
   cd backend
   python migrations/001_add_custom_reminders.py
   python migrations/002_add_dynamic_fields.py
   python migrations/003_add_email_verification.py
   python migrations/004_add_password_reset.py
   python migrations/005_add_preferences.py
   ```

3. **Verify migration success:**
   - Check console output for success messages
   - Test the application to ensure everything works

## Migration Naming Convention

Format: `{number}_{description}.py`

- **Number**: Three-digit sequential number (001, 002, etc.)
- **Description**: Brief snake_case description of what the migration does

Examples:
- `001_add_custom_reminders.py`
- `002_add_dynamic_fields.py`
- `003_add_email_verification.py`

## Available Migrations

| Number | File | Description |
|--------|------|-------------|
| 001 | add_custom_reminders.py | Adds custom reminder functionality to items |
| 002 | add_dynamic_fields.py | Adds support for dynamic/custom fields per item type |
| 003 | add_email_verification.py | Adds email verification token and status fields |
| 004 | add_password_reset.py | Adds password reset token and expiry fields |
| 005 | add_preferences.py | Adds user preferences for display settings |

## Creating New Migrations

When creating a new migration:

1. **Determine the next number** in sequence
2. **Name it descriptively** using snake_case
3. **Include proper error handling** and rollback logic if possible
4. **Test thoroughly** on a backup database first
5. **Document** the migration in this README

Example template:
```python
"""
Migration: Add feature_name
Description: Brief description of what this migration does
"""
import sqlite3
from datetime import datetime

def migrate():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # Your migration SQL here
        cursor.execute('''
            ALTER TABLE table_name 
            ADD COLUMN new_column TEXT
        ''')
        
        conn.commit()
        print("✅ Migration completed successfully")
        
    except Exception as e:
        print(f"❌ Migration failed: {e}")
        conn.rollback()
        raise
    finally:
        conn.close()

if __name__ == "__main__":
    migrate()
```

## Troubleshooting

### Migration fails with "database is locked"
- Ensure the application is not running
- Close any database browser tools
- Check for stale connections

### Migration partially completed
- Restore from backup: `cp database.db.backup database.db`
- Fix the migration script
- Run again

### Need to rollback a migration
- Restore from backup taken before migration
- If no backup exists, manually reverse the changes using SQL

## Best Practices

1. **Always backup before migrating** - Cannot stress this enough!
2. **Test on a copy first** - Run migration on a database copy
3. **Run in order** - Never skip migrations
4. **One change per migration** - Keep migrations focused
5. **Make migrations idempotent** - Safe to run multiple times if possible
6. **Document everything** - Update this README with each new migration

## Non-Interactive Initialization (Docker / CI)

To run `init_db.py` without an interactive prompt (e.g., in Docker or CI pipelines):
```bash
python init_db.py --force
```

This will skip the confirmation prompt and overwrite the existing database automatically.
