from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


class DBClient(object):

    def __init__(self, db_config):
        url = f"mysql+aiomysql://{db_config.user}:{db_config.pwd}@{db_config.HOST}:{db_config.PORT}/{db_config.db}"
        self.engine = create_async_engine(url)
        self.SessionLocal = AsyncSession(bind=self.engine, autocommit=False, autoflush=False)

