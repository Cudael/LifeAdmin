import shutil
import os
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def backup_database():
    """Create a timestamped backup of the database"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = "backups"
    
    # Create backups directory if it doesn't exist
    os.makedirs(backup_dir, exist_ok=True)
    
    # Copy database
    source = "database.db"
    destination = f"{backup_dir}/database_backup_{timestamp}.db"
    
    if os.path.exists(source):
        try:
            shutil.copy2(source, destination)
            logger.info(f"✅ Database backed up to: {destination}")
            
            # Keep only last 7 backups
            backups = sorted([
                f for f in os.listdir(backup_dir) 
                if f.startswith("database_backup_") and f.endswith(".db")
            ])
            
            if len(backups) > 7:
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
    else:
        logger.error("❌ Database file not found")
        return False

if __name__ == "__main__":
    backup_database()