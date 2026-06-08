from pydantic import BaseModel, EmailStr


class CreateUserModel(BaseModel):
    email: EmailStr
    username: str
    password_hash: str
