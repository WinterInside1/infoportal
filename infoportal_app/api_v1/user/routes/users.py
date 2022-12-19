from typing import List

from fastapi import APIRouter, Depends

from apps.user.schemas.user import (
    GetUserSchema,
    CreateUserSchema,
    GetUserListSchema,
    UpdateUserSchema,
)
from apps.user.services.user import UserService
from core.auth.permissions import PermissionDependency, ApiKey, AllowAll


users_router = APIRouter(prefix='/users')

@users_router.post(
    "",
    response_model=GetUserSchema,
    dependencies=[Depends(PermissionDependency([AllowAll]))],
    tags=["Public"],
)
async def create_user(body: CreateUserSchema):
    return await UserService.create_user(body)


@users_router.get(
    "/{user_id}",
    response_model=GetUserSchema,
    dependencies=[Depends(PermissionDependency([ApiKey]))],
)
async def get_user(user_id: int):
    return await UserService.get_user(user_id)


@users_router.get(
    "",
    response_model=List[GetUserListSchema],
    dependencies=[Depends(PermissionDependency([ApiKey]))],
)
async def get_user_list(page: int, page_size: int = 20):
    return await UserService.get_user_list(page=page, page_size=page_size)


@users_router.put(
    "/{user_id}",
    response_model=UpdateUserSchema,
    dependencies=[Depends(PermissionDependency([ApiKey]))],
)
async def update_user(user_id: int, body: UpdateUserSchema):
    return await UserService.update_user(user_id=user_id, user_update=body)


@users_router.delete(
    "/{user_id}",
    dependencies=[Depends(PermissionDependency([ApiKey]))],
)
async def delete_user(user_id: int):
    await UserService.delete_user(user_id)
