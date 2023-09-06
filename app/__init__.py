from app.core.config import DB_SETTING
from app.db.db_client import DBConnect

db_client = DBConnect(DB_SETTING)

__version__ = "0.1.0"
