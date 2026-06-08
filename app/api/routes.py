from fastapi import APIRouter
from app.api.routers.user import user_router

master_router = APIRouter()

master_router.include_router(user_router, prefix="/auth", tags=["Users"])
