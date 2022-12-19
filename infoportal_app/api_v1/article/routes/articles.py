from typing import List

from fastapi import APIRouter, Depends

from apps.article.schemas.user import (
    GetUserSchema,
    CreateUserSchema,
    GetUserListSchema,
    UpdateUserSchema,
)
from apps.article.services.user import UserService
from core.auth.permissions import PermissionDependency, ApiKey, AllowAll


users_router = APIRouter(prefix='/users')
