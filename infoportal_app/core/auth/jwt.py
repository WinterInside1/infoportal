from typing import TypeVar, Generic, Type

import ormar
from fastapi import Depends
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel

from core.utils.crud_base import CRUDBase


class TokenPayload(BaseModel):
    id: int


UserModelType = TypeVar("UserModelType", bound=ormar.Model)
TokenPayloadSchema = TypeVar("TokenPayloadSchema", bound=TokenPayload)
Crud = CRUDBase[UserModelType]


class JWT(Generic[UserModelType, TokenPayloadSchema]):
    def __init__(self, user_model: Type[UserModelType]):
        self.user_model = user_model
        self.user_crud: CRUDBase[UserModelType] = Crud(user_model)

    async def get_current_user(self, Authorize: AuthJWT = Depends()) -> UserModelType:
        Authorize.jwt_required()
        current_user_id = Authorize.get_jwt_subject()
        return await self.user_crud.get(current_user_id)
