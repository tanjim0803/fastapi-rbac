from fastapi import APIRouter
from app.database.session import SessionDep
from app.schemas.user import CreateUserModel, ReadUserModel
from app.services.user import user_service

user_router = APIRouter()


@user_router.post("/", response_model=ReadUserModel)
async def register_user(session: SessionDep, user_data: CreateUserModel):
    user = await user_service.create_user(session, user_data)

    return user
