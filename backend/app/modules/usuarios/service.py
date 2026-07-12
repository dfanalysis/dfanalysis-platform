from uuid import UUID

from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.modules.auth.models import Perfil
from app.modules.usuarios.models import Usuario
from app.modules.usuarios.repository import UsuarioRepository


class UsuarioService:
    """Regras de negócio para criação e consulta de usuários."""

    def __init__(self, db: Session) -> None:
        self.db = db
        self.repository = UsuarioRepository(db)

    def get_or_create(
        self,
        *,
        empresa_id: UUID,
        nome: str,
        email: str,
        password: str,
        profiles: list[Perfil] | None = None,
    ) -> tuple[Usuario, bool]:
        """
        Retorna o usuário existente ou cria uma nova conta.

        O segundo item da tupla informa se o registro foi criado.
        """

        normalized_email = email.strip().lower()

        existing_user = self.repository.get_by_email(normalized_email)

        if existing_user:
            return existing_user, False

        if len(password) < 12:
            raise ValueError(
                "A senha inicial deve possuir pelo menos 12 caracteres."
            )

        user = Usuario(
            empresa_id=empresa_id,
            nome=nome.strip(),
            email=normalized_email,
            password_hash=hash_password(password),
        )

        if profiles:
            user.perfis.extend(profiles)

        return self.repository.add(user), True