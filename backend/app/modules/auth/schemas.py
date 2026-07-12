from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator


class LoginRequest(BaseModel):
    email: str = Field(
        ...,
        min_length=5,
        max_length=255,
        examples=["admin@empresa.com.br"],
    )
    password: str = Field(
        ...,
        min_length=1,
        max_length=128,
        examples=["SenhaSegura123!"],
    )

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: str) -> str:
        normalized_email = value.strip().lower()

        if "@" not in normalized_email:
            raise ValueError("Informe um e-mail válido.")

        return normalized_email


class AuthenticatedUserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    empresa_id: UUID
    nome: str
    email: str
    profiles: list[str]
    last_login_at: datetime | None


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    expires_in: int
    user: AuthenticatedUserResponse


class ApiErrorResponse(BaseModel):
    detail: str
