from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

# create the database engine
engine = create_async_engine(DATABASE_URL, echo=True)

#create a session factory
async_session = sessionmaker(
    bind=engine, expire_on_commit=False, class_=AsyncSession
)

#Dependency to get the database session
async def get_db():
    async with async_session as session
    yield session
