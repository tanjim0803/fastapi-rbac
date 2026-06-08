from pydantic import BaseModel, EmailStr
import uuid


class ReadUserModel(BaseModel):
    id: uuid.UUID
    email: EmailStr
    username: str
    password_hash: str


class CreateUserModel(BaseModel):
    email: EmailStr
    username: str
    password: str
