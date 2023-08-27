from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, JSON


Base = declarative_base()


class Context(Base):
    __tablename__ = 'context'

    id = Column(Integer, primary_key=True)
    id_user = Column(Integer)
    data = Column(JSON)


class AsyncDatabase:

    def __init__(self):
        self.db_url = "sqlite+aiosqlite:///db/context.db"
        self.engine = create_async_engine(self.db_url)
        self.session = sessionmaker(self.engine, class_=AsyncSession, expire_on_commit=False)

    async def __aenter__(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
            return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.engine.dispose()

    async def execute(self, query):
        async with self.session() as session:
            async with session.begin():
                result = await session.execute(query)
                await session.commit()
                return result

    async def fetch(self, query):
        result = await self.execute(query)
        return result.fetchone()

    async def add(self, query):
        async with self.session() as session:
            session.add(query)
            await session.commit()


async def db_main():
    async with AsyncDatabase() as db:
        return db
