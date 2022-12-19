from fastapi import FastAPI
from sqladmin import Admin

from auth import AuthBackend
from views import *
from config import config


app = FastAPI()

authentication_backend = AuthBackend(secret_key=config.SECRET_KEY)
admin = Admin(app, engine, authentication_backend=authentication_backend)


for _, view in admin_views:
    admin.add_view(view)
