from datetime import datetime, timedelta, timezone
from typing import Any
from uuid import UUID

from jose import JWTError, jwt
from pwdlib import PasswordHash

from app.core.config import settings


password_hasher = PasswordHash.recommended()


class InvalidAccessTokenError(Exception):
    """Token JWT ausente, inválido, expirado ou incompatível."""


def hash_password(password: str) -> str:
    """
    Gera hash seguro de senha usando Argon2.

    A senha em texto puro nunca deve ser persistida.
    """
    return password_hasher.hash(password)


def verify_password(password: str, password_hash: str) -> bool:
    """
    Compara uma senha em texto puro com seu hash persistido.

    Retorna False para hashes malformados, evitando exposição
    de detalhes internos de segurança.
    """
    try:
        return password_hasher.verify(password, password_hash)
    except Exception:
        return False


def create_access_token(
    *,
    user_id: UUID,
    empresa_id: UUID,
    profile_codes: list[str],
) -> str:
    """
    Cria um access token de curta duração.

    O token não armazena dados sensíveis, como senha, e-mail,
    CNPJ ou permissões detalhadas.
    """
    if not settings.JWT_SECRET:
        raise RuntimeError(
            "JWT_SECRET não está configurado. "
            "Defina uma chave segura no arquivo .env."
        )

    now = datetime.now(timezone.utc)
    expires_at = now + timedelta(
        minutes=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload: dict[str, Any] = {
        "sub": str(user_id),
        "empresa_id": str(empresa_id),
        "profiles": profile_codes,
        "type": "access",
        "iat": now,
        "exp": expires_at,
        "iss": settings.JWT_ISSUER,
        "aud": settings.JWT_AUDIENCE,
    }

    return jwt.encode(
        payload,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM,
    )


def decode_access_token(token: str) -> dict[str, Any]:
    """Valida assinatura, expiração, issuer, audience e tipo do token."""
    if not settings.JWT_SECRET:
        raise InvalidAccessTokenError("JWT_SECRET não está configurado.")

    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
            issuer=settings.JWT_ISSUER,
            audience=settings.JWT_AUDIENCE,
        )
    except JWTError as error:
        raise InvalidAccessTokenError("Token inválido ou expirado.") from error

    if payload.get("type") != "access":
        raise InvalidAccessTokenError("Tipo de token inválido.")

    if not payload.get("sub"):
        raise InvalidAccessTokenError("Token sem identificador de usuário.")

    return payload
