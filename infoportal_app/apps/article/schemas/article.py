from pydantic import BaseModel


class GetArticleListSchema(BaseModel):
    id: int
    name: str
    category: str
    description: str


class CreateArticleSchema(BaseModel):
    name: str
    category: str
    description: str


class GetArticleSchema(BaseModel):
    id: int
    name: str
    category: str
    description: str


class UpdateArticleSchema(BaseModel):
    name: str
    category: str
    description: str

