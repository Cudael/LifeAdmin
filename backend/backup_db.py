import sqlite3
import os
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def backup_database():
    """Create a timestamped, WAL-safe backup of the SQLite database."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = "backups"
    os.makedirs(backup_dir, exist_ok=True)

    source = "database.db"
    destination = f"{backup_dir}/database_backup_{timestamp}.db"

    if not os.path.exists(source):
        logger.error("❌ Database file not found")
        return False

    try:
        source_conn = sqlite3.connect(source)
        dest_conn = sqlite3.connect(destination)
        source_conn.backup(dest_conn)  # Atomic, WAL-checkpoint-safe
        dest_conn.close()
        source_conn.close()
        logger.info(f"✅ Database backed up to: {destination}")

        # Keep only last 7 backups
        backups = sorted([
            f for f in os.listdir(backup_dir)
            if f.startswith("database_backup_") and f.endswith(".db")
        ])
        for old_backup in backups[:-7]:
            try:
                os.remove(f"{backup_dir}/{old_backup}")
                logger.info(f"🗑️  Removed old backup: {old_backup}")
            except Exception as e:
                logger.error(f"Failed to remove {old_backup}: {e}")

        return True
    except Exception as e:
        logger.error(f"❌ Backup failed: {e}")
        return False

if __name__ == "__main__":
    backup_database()