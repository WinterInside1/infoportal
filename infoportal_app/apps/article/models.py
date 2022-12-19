from datetime import datetime, timedelta
import ormar
from core.db.database import BaseMeta, BaseModel
from datetime import datetime

class User(BaseModel):
    class Meta(BaseMeta):
        pass

    id = ormar.Integer(primary_key=True)
    name = ormar.String(max_length=128, nullable=True)
    category = ormar.String(max_length=128)
    description = ormar.String(max_length=1280)
    date = ormar.DateTime(default=datetime.now())
