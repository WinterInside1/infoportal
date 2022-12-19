from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from config import config


engine = create_engine(
    config.DB_URL
)

Base = declarative_base()
Base.metadata.reflect(engine)
