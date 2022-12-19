from fastapi import APIRouter

from api_v1.user.router import user_router

router = APIRouter(prefix="/api/v1")

router.include_router(user_router)
