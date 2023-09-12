from demo_1.core.config import DB_CONFIG
from demo_1.db.db_client import DBClient

db_client = DBClient(DB_CONFIG)

__version__ = "0.1.0"
