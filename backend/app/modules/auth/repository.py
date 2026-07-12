from datetime import datetime
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session, selectinload

from app.modules.usuarios.models import Usuario


class AuthRepository:
    """Persistência necessária para os casos de uso de autenticação."""

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_user_by_email(self, email: str) -> Usuario | None:
        statement = (
            select(Usuario)
            .where(func.lower(Usuario.email) == email.strip().lower())
            .options(selectinload(Usuario.perfis))
        )

        return self.db.scalar(statement)

    def get_user_by_id(self, user_id: UUID) -> Usuario | None:
        statement = (
            select(Usuario)
            .where(Usuario.id == user_id)
            .options(selectinload(Usuario.perfis))
        )

        return self.db.scalar(statement)

    def update_last_login(self, user: Usuario, logged_at: datetime) -> None:
        user.last_login_at = logged_at
        self.db.add(user)
        self.db.flush()
