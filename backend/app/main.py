from fastapi import FastAPI

from app.api.database import router as database_router
from app.core.config import settings
from app.core.logger import logger
from app.db import model_registry  # noqa: F401
from app.modules.auth.router import router as auth_router
from app.modules.fiscal.solicitacoes.router import (
    router as solicitacoes_router,
)


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


app.include_router(database_router)
app.include_router(auth_router)
app.include_router(solicitacoes_router)


@app.get("/")
def root() -> dict[str, str]:
    logger.info("API iniciada.")

    return {
        "application": settings.APP_NAME,
        "status": "running",
    }