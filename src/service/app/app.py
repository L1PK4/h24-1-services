from contextlib import asynccontextmanager
from fastapi import FastAPI
from service.app.routes.v1 import router
from service.app.settings import Settings, get_settings
from service.infrastructure.sqlalchemy.session_manager import session_manager


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    await session_manager.initialize(settings.DB_DSN)
    try:
        yield
    finally:
        await session_manager.close()


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan, docs_url="/docs", redoc_url="/redoc")
    app.include_router(router.router)
    return app
