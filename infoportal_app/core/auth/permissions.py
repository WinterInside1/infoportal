from abc import ABC, abstractmethod
from typing import List, Type

from fastapi import Request
from fastapi.openapi.models import APIKey, APIKeyIn
from fastapi.security.base import SecurityBase

from core.auth.api_key import api_keys_in_env
from core.exceptions import CustomException, UnauthorizedException


auth_header = "x_api_key"


class BasePermission(ABC):
    exception = CustomException

    @abstractmethod
    async def has_permission(self, request: Request) -> bool:
        pass


class ApiKey(BasePermission):
    exception = UnauthorizedException

    async def has_permission(self, request: Request) -> bool:
        x_api_key = request.headers.get(auth_header)
        if x_api_key not in api_keys_in_env():
            return False
        return True


class AllowAll(BasePermission):
    async def has_permission(self, request: Request) -> bool:
        return True


class PermissionDependency(SecurityBase):
    def __init__(self, permissions: List[Type[BasePermission]]):
        self.permissions = permissions
        self.model: APIKey = APIKey(**{"in": APIKeyIn.header}, name=auth_header)
        self.scheme_name = self.__class__.__name__

    async def __call__(self, request: Request):
        for permission in self.permissions:
            cls = permission()
            if not await cls.has_permission(request=request):
                raise cls.exception
