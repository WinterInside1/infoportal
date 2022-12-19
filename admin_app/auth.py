import jwt
from fastapi import Request
from sqladmin.authentication import AuthenticationBackend

#from config import config
from config import config


class AuthBackend(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        if (username := form.get("username")) == config.ADMIN_USER\
                and form.get("password") == config.ADMIN_PASS:
            encoded_jwt = jwt.encode({"username": username}, config.SECRET_KEY, algorithm="HS256")
            request.session.update({"token": encoded_jwt.decode("utf-8")})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")
        if not token:
            return False
        decoded_jwt = jwt.decode(token, config.SECRET_KEY, algorithms=["HS256"])
        return True
