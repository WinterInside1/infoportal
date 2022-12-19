from core.utils.crud_base import CRUDBase
from apps.user.models import Article
from apps.user.schemas.article import CreateArticleSchema, UpdateArticleSchema


class CRUDUser(CRUDBase[Article, CreateArticleSchema, UpdateArticleSchema]):
    ...


article = CRUDUser(Article)
