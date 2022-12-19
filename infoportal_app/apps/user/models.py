from datetime import datetime, timedelta
import ormar
from core.db.database import BaseMeta, BaseModel


class User(BaseModel):
    class Meta(BaseMeta):
        pass

    id = ormar.Integer(primary_key=True)
    username = ormar.String(max_length=128, nullable=True)
    email = ormar.String(max_length=128)
    pswd = ormar.String(max_length=128)
    position = ormar.String(max_length=128)


