from fastapi import APIRouter

from api_v1.user.routes.users import users_router

user_router = APIRouter()

user_router.include_router(users_router, tags=["Users"])
