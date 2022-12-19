from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from alembic.config import Config
from alembic import command

from config import config
from fastapi.middleware.cors import CORSMiddleware
from core.exceptions import CustomException
from core.middlwares.logger import log_requests_dependency, log_errors_middleware
from core.db.database import database
from api_v1.router import router


def run_migrations(script_location: str, dsn: str) -> None:
    alembic_cfg = Config('alembic.ini')
    alembic_cfg.set_main_option('script_location', script_location)
    alembic_cfg.set_main_option('sqlalchemy.url', dsn)
    command.upgrade(alembic_cfg, 'head')


def init_database(app_: FastAPI) -> None:
    @app_.on_event("startup")
    async def startup() -> None:
        await database.connect()

    @app_.on_event("shutdown")
    async def shutdown() -> None:
        await database.disconnect()


def init_routers(app_: FastAPI) -> None:
    app_.include_router(router)


def init_middleware(app_: FastAPI) -> None:
    app_.middleware("http")(log_errors_middleware)


def init_listeners(app_: FastAPI) -> None:
    @app_.exception_handler(CustomException)
    async def custom_exception_handler(request: Request, exc: CustomException):
        return JSONResponse(
            status_code=exc.code,
            content={"error_code": exc.error_code, "message": exc.message},
        )


app = FastAPI()

# origins = [
#     "http://localhost:",
#     "http://localhost:8080",
# `"http://localhost:",
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Hide",
        description="Hide API",
        version="1.0.0",
        docs_url=None if config.ENV == "production" else "/docs",
        redoc_url=None if config.ENV == "production" else "/redoc",
        dependencies=[Depends(log_requests_dependency)]
    )
    FastAPI(root_path="/zalupa")
    run_migrations("./migrations", config.DB_URL_SYNC)
    init_database(app_)
    init_routers(app_)
    init_middleware(app_)
    init_listeners(app_)
    return app_


app = create_app()
