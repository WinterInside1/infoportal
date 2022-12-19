import databases
from pydantic.annotated_types import Any

import ormar
import sqlalchemy

from config import config

database = databases.Database(config.DB_URL)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class BaseModel(ormar.Model):
    def extract_foreign_keys_names(self):
        model_fields_names = {column.key for column in self.Meta.columns}
        model_foreign_keys_names = model_fields_names & self.extract_related_names()
        return model_foreign_keys_names

    def dict(self, *args, **kwargs) -> dict[str, Any]:
        dict_instance = super().dict(*args, **kwargs)

        for foreign_key_field in self.extract_foreign_keys_names():
            if (foreign_key := dict_instance.get(foreign_key_field)) is not None:
                if "id" in foreign_key and len(foreign_key.keys()) == 1:
                    dict_instance.update({foreign_key_field: foreign_key["id"]})

        return dict_instance
