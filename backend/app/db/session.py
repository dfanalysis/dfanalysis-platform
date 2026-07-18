from collections.abc import Generator

from sqlalchemy.orm import Session, sessionmaker

from app.db.database import engine


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
)


def get_db() -> Generator[Session, None, None]:
    """
    Fornece uma sessão SQLAlchemy para cada requisição.

    A sessão é encerrada automaticamente ao final da operação,
    inclusive quando ocorre uma exceção.
    """

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


__all__ = [
    "SessionLocal",
    "get_db",
]