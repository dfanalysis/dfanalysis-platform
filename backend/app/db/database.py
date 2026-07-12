from sqlalchemy import Engine, create_engine

from app.core.config import settings


DATABASE_URL = settings.database_url

engine: Engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
    pool_size=5,
    max_overflow=10,
    pool_recycle=1800,
)
