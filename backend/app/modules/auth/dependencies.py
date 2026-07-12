from typing import Annotated
from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.security import InvalidAccessTokenError, decode_access_token
from app.db.session import get_db
from app.modules.auth.exceptions import AuthenticatedUserNotFoundError
from app.modules.auth.service import AuthService
from app.modules.usuarios.models import Usuario


bearer_scheme = HTTPBearer(
    auto_error=False,
    scheme_name="JWT Access Token",
)


def get_current_user(
    credentials: Annotated[
        HTTPAuthorizationCredentials | None,
        Depends(bearer_scheme),
    ],
    db: Annotated[Session, Depends(get_db)],
) -> Usuario:
    """
    Resolve e valida o usuário autenticado da requisição.

    A consulta ao banco evita que um JWT ainda válido permita acesso
    a usuários, empresas ou tenants desativados.
    """
    unauthorized_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Não foi possível autenticar as credenciais informadas.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    if credentials is None:
        raise unauthorized_exception

    try:
        payload = decode_access_token(credentials.credentials)
        user_id = UUID(payload["sub"])
        user = AuthService(db).get_authenticated_user(user_id)
    except (
        InvalidAccessTokenError,
        AuthenticatedUserNotFoundError,
        ValueError,
        KeyError,
    ):
        raise unauthorized_exception

    return user


CurrentUser = Annotated[Usuario, Depends(get_current_user)]
