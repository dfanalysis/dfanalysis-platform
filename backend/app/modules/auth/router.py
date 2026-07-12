from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import get_db
from app.modules.auth.dependencies import CurrentUser
from app.modules.auth.exceptions import InvalidCredentialsError
from app.modules.auth.schemas import (
    ApiErrorResponse,
    AuthenticatedUserResponse,
    LoginRequest,
    LoginResponse,
)
from app.modules.auth.service import AuthService
from app.modules.usuarios.models import Usuario


router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Autenticação"],
)


def serialize_user(user: Usuario) -> AuthenticatedUserResponse:
    return AuthenticatedUserResponse(
        id=user.id,
        empresa_id=user.empresa_id,
        nome=user.nome,
        email=user.email,
        profiles=[
            profile.codigo
            for profile in user.perfis
            if profile.is_active
        ],
        last_login_at=user.last_login_at,
    )


@router.post(
    "/login",
    response_model=LoginResponse,
    status_code=status.HTTP_200_OK,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "model": ApiErrorResponse,
            "description": "Credenciais inválidas.",
        },
    },
)
def login(
    payload: LoginRequest,
    db: Annotated[Session, Depends(get_db)],
) -> LoginResponse:
    try:
        user, access_token = AuthService(db).login(
            email=payload.email,
            password=payload.password,
        )
    except InvalidCredentialsError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="E-mail ou senha inválidos.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return LoginResponse(
        access_token=access_token,
        expires_in=settings.JWT_ACCESS_TOKEN_EXPIRE_MINUTES * 60,
        user=serialize_user(user),
    )


@router.get(
    "/me",
    response_model=AuthenticatedUserResponse,
    status_code=status.HTTP_200_OK,
)
def get_me(current_user: CurrentUser) -> AuthenticatedUserResponse:
    return serialize_user(current_user)
