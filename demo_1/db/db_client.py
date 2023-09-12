from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession


class DBClient(object):
    """A class to manage the database connection."""

    def __init__(self, db_config):
        url = f"mysql+aiomysql://{db_config.user}:{db_config.pwd}@{db_config.HOST}:{db_config.PORT}/{db_config.db}"
        self.engine = create_async_engine(url)
        self.Session = AsyncSession(bind=self.engine)

    async def insert(self, obj):
        """Insert an object into the database."""
        async with self.Session as session:  # 创建会话
            async with session.begin():  # 开启事务
                session.add(obj)  # 添加对象
            await session.commit()  # 提交事务
            await session.refresh(obj)  # 刷新对象
            return obj  # 返回插入的对象

    async def select(self, sql, s):
        """Select an object from the database."""
        result = await s.execute(sql)  # 执行sql语句
        return result  # 返回查询结果集

    async def update(self, obj):
        """Update an object in the database."""
        async with self.Session as session:
            async with session.begin():
                session.add(obj)
            await session.commit()
            await session.refresh(obj)
            return obj

    async def delete(self, obj):
        """Delete an object from the database."""
        async with self.Session as session:
            async with session.begin():
                await session.delete(obj)
            await session.commit()
            return obj
