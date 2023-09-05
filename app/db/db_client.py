from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


class DBConnect(object):
    def __init__(self, db_setting):
        url = f"mysql+aiomysql://{db_setting.user}:{db_setting.pwd}@{db_setting.host}:{db_setting.port}/{db_setting.db}"
        self.engine = create_async_engine(url)
        self.Session = AsyncSession(bind=self.engine)

    async def insert(self, obj):
        async with self.Session as session:
            async with session.begin():
                session.add(obj)
            await session.commit()

    async def select(self, sql):
        async with self.Session as session:
            async with session.begin():
                result = await session.execute(sql)
                return result
