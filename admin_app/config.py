import os

from pydantic import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class Config(BaseSettings):
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

    SECRET_KEY: str = os.getenv("SECRET_KEY")

    ADMIN_USER: str = os.getenv("ADMIN_USER")
    ADMIN_PASS: str = os.getenv("ADMIN_PASS")

    DB_USER: str = os.getenv("POSTGRES_USER")
    BD_NAME: str = os.getenv("POSTGRES_DB")
    BD_PASS: str = os.getenv("POSTGRES_PASSWORD")
    BD_HOST: str = os.getenv("POSTGRES_HOST")
    BD_PORT: int = os.getenv("POSTGRES_PORT")
    DB_URL: str = f"postgresql+psycopg2://{DB_USER}:{BD_PASS}@{BD_HOST}:{BD_PORT}/{BD_NAME}"


config: Config = Config()
