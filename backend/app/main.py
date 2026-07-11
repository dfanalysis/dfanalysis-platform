from fastapi import FastAPI

from app.api.database import router as database_router
from app.core.config import settings
from app.core.logger import logger

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(database_router)


@app.get("/")
def root():
    logger.info("API iniciada.")

    return {
        "application": settings.APP_NAME,
        "status": "running",
    }