from sqlmodel import SQLModel, create_engine
from models.user import User
from models.item import Item
from models.item_type import ItemType
from models.notification import Notification

# Create engine - using the correct database name!
engine = create_engine("sqlite:///database.db", echo=True)

# Create all tables
SQLModel.metadata.create_all(engine)

print("✅ Database tables created in database.db!")
