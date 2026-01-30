from urllib.parse import quote
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
from shared.config import settings

encoded_password = quote(settings.DB_PASSWORD)
SQLALCHEMY_DATABASE_URL =       f"mysql+pymysql://{settings.DB_USER}:{encoded_password}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_DATABASE}"
SQLALCHEMY_DATABASE_ASYNC_URL = f"mysql+asyncmy://{settings.DB_USER}:{encoded_password}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_DATABASE}"


Base = declarative_base()



## Engine and Sessions - Sync
def get_engine():
    db_engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False, poolclass=QueuePool, pool_pre_ping=True)
    return db_engine

engine = get_engine()
SessionFactory = sessionmaker(autocommit=False, autoflush=False, expire_on_commit=False, bind=engine)

## Engine and Sessions - Async
def get_async_engine():
    db_engine = create_async_engine(SQLALCHEMY_DATABASE_ASYNC_URL, pool_pre_ping=True)
    return db_engine

async_engine = get_async_engine()
AsyncSessionFactory = async_sessionmaker(autocommit=False, autoflush=False, expire_on_commit=False, bind=async_engine)



# DB dependency - sync
def get_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()

# DB dependency - async
async def get_async_db():
    db = AsyncSessionFactory()
    try:
        yield db
    finally:
        await db.close()



        