from sqlmodel import SQLModel, Field
from pydantic import EmailStr
import uuid


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4(), primary_key=True, nullable=False
    )
    email: EmailStr
    username: str
    password_hash: str

    def __repr__(self):
        return f"<User {self.username}>"
