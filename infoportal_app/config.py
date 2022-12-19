import os

from pydantic import BaseSettings
from dotenv import load_dotenv


load_dotenv()


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8080

    DB_USER: str = os.getenv("POSTGRES_USER")
    DB_NAME: str = os.getenv("POSTGRES_DB")
    DB_PASS: str = os.getenv("POSTGRES_PASSWORD")
    DB_HOST: str = os.getenv("POSTGRES_HOST")
    DB_PORT: int = os.getenv("POSTGRES_PORT")
    DB_URL: str = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    DB_URL_SYNC: str = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    JWT_SECRET_KEY: str = None
    JWT_ALGORITHM: str = None
    SENTRY_SDN: str = None
    CELERY_BROKER_URL: str = "amqp://user:123@localhost:5672/"
    CELERY_BACKEND_URL: str = "redis://:password123@localhost:6379/0"
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    API_KEY_PREFIX: str = "API_KEY_"


class DevelopmentConfig(Config):
    pass


class LocalConfig(Config):
    pass


class ProductionConfig(Config):
    DEBUG: str = False


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "dev": DevelopmentConfig(),
        "local": LocalConfig(),
        "prod": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
