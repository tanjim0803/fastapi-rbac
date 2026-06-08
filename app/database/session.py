from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.config import db_settings
from typing import Annotated
from fastapi import Depends

DATABASE_URL = db_settings.DATABASE_URL

async_engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = async_sessionmaker(bind=async_engine, expire_on_commit=False)


async def create_tables():
    async with async_engine.begin() as conn:
        from .models import User

        await conn.run_sync(SQLModel.metadata.create_all)


async def get_session():

    async with AsyncSessionLocal() as session:
        yield session


SessionDep = Annotated[AsyncSession, Depends(get_session)]
