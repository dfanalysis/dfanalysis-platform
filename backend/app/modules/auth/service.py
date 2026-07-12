from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy.orm import Session

from app.core.security import create_access_token, verify_password
from app.modules.auth.exceptions import (
    AuthenticatedUserNotFoundError,
    InvalidCredentialsError,
)
from app.modules.auth.repository import AuthRepository
from app.modules.usuarios.models import Usuario


class AuthService:
    """
    Regras de negócio do módulo de autenticação.

    Esta camada concentra validação de credenciais,
    atualização de último acesso,
    emissão do JWT
    e recuperação do usuário autenticado.
    """

    def __init__(self, db: Session) -> None:
        self.db = db
        self.repository = AuthRepository(db)

    def login(
        self,
        *,
        email: str,
        password: str,
    ) -> tuple[Usuario, str]:
        """
        Realiza autenticação do usuário.

        Fluxo:

        1. Busca usuário.
        2. Valida status.
        3. Valida senha.
        4. Gera JWT.
        5. Atualiza último acesso.
        6. Retorna usuário + token.
        """

        user = self.repository.get_user_by_email(email)

        if not self._is_user_allowed_to_authenticate(user):
            raise InvalidCredentialsError()

        if not verify_password(password, user.password_hash):
            raise InvalidCredentialsError()

        # O token é criado antes do commit para evitar registrar
        # um login caso a emissão do JWT falhe.
        access_token = self._issue_access_token(user)

        try:
            self.repository.update_last_login(
                user=user,
                logged_at=datetime.now(timezone.utc),
            )

            self.db.commit()
            self.db.refresh(user)

        except Exception:
            self.db.rollback()
            raise

        return user, access_token

    def get_authenticated_user(self, user_id: UUID) -> Usuario:
        """
        Recupera o usuário autenticado a partir do JWT.
        """

        user = self.repository.get_user_by_id(user_id)

        if not self._is_user_allowed_to_authenticate(user):
            raise AuthenticatedUserNotFoundError()

        return user

    @staticmethod
    def _is_user_allowed_to_authenticate(
        user: Usuario | None,
    ) -> bool:
        """
        Valida se o usuário pode autenticar.

        Além do usuário, também verifica
        o estado da empresa (tenant).
        """

        return bool(
            user
            and user.is_active
            and user.deleted_at is None
            and user.empresa is not None
            and user.empresa.is_active
            and user.empresa.deleted_at is None
        )

    @staticmethod
    def _issue_access_token(user: Usuario) -> str:
        """
        Cria um Access Token contendo apenas
        informações necessárias para autenticação.
        """

        active_profile_codes = [
            profile.codigo
            for profile in user.perfis
            if profile.is_active
        ]

        return create_access_token(
            user_id=user.id,
            empresa_id=user.empresa_id,
            profile_codes=active_profile_codes,
        )