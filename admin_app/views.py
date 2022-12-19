import inspect
import sys
from typing import Any

from sqladmin import ModelView
from sqladmin.helpers import get_column_python_type
from sqlalchemy import select
from sqlalchemy.orm import joinedload, sessionmaker

from db import engine
from models import *


session = sessionmaker(expire_on_commit=False, bind=engine)()


class UserAdmin(ModelView, model=User):
    name = "User"
    name_plural = "Users"
    column_list = [User.id, User.email, User.username, User.pswd, User.position]
    column_details_list = column_list
    column_sortable_list = [User.id]
    column_default_sort = ("id", True)


def is_admin_view(o: object) -> bool:
    return inspect.isclass(o) and issubclass(o, ModelView) and o.__name__.endswith("Admin")


admin_views = inspect.getmembers(sys.modules[__name__], is_admin_view)
