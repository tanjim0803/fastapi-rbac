from fastapi import APIRouter, Depends, HTTPException, status
from app.database.session import SessionDep
from app.schemas.user import CreateUserModel, ReadUserModel
from app.services.user import user_service
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from app.utils import verify_password_hash

user_router = APIRouter()


@user_router.post("/register", response_model=ReadUserModel)
async def register_user(session: SessionDep, user_data: CreateUserModel):
    user = await user_service.create_user(session, user_data)

    return user


@user_router.post("/login")
async def login(
    session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = await user_service.user_exists(session, form_data.username)

    if not user or not verify_password_hash(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email or Password Invalid!"
        )

    return {"token": user.id}
