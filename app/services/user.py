from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.user import CreateUserModel
from sqlmodel import select
from app.database.models import User
from fastapi import HTTPException
from app.utils import create_password_hash


class UserService:
    async def user_exists(self, session: AsyncSession, email: str):
        statement = select(User).where(User.email == email)
        results = await session.execute(statement)

        user = results.scalar_one_or_none()

        return user if user else False

    async def create_user(self, session: AsyncSession, user_data: CreateUserModel):
        user = await self.user_exists(session, user_data.email)

        if user:
            raise HTTPException(status_code=400, detail="This user already exists!")

        new_user = User(
            **user_data.model_dump(exclude=["password"]),
            password_hash=create_password_hash(user_data.password),
        )

        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)

        return new_user


user_service = UserService()
