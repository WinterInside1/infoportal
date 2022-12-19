from core.utils.crud_base import CRUDBase
from apps.user.models import User
from apps.user.schemas.user import CreateUserSchema, UpdateUserSchema


class CRUDUser(CRUDBase[User, CreateUserSchema, UpdateUserSchema]):
    ...


user = CRUDUser(User)
