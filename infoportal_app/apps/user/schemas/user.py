from dataclasses import Field
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class GetUserListSchema(BaseModel):
    id: int
    username: str
    email: str
    position: str


class CreateUserSchema(BaseModel):
    username: str
    email: str
    pswd: str
    position: str


class GetUserSchema(BaseModel):
    id: int
    username: str
    email: str
    position: str


class UpdateUserSchema(BaseModel):
    username: str
    email: str
    position: str

