from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.modules.operacoes.inbox.enums import (
    CanalEntrada,
    OrigemProcessamento,
    StatusInboxMessage,
)


class InboxMessageCreate(BaseModel):
    """Payload para registro de uma comunicação recebida."""

    canal: CanalEntrada
    origem_processamento: OrigemProcessamento

    message_id_externo: str | None = Field(
        default=None,
        max_length=255,
    )

    assunto: str = Field(
        ...,
        min_length=1,
        max_length=500,
    )

    corpo: str = Field(
        ...,
        min_length=1,
    )

    remetente: str = Field(
        ...,
        min_length=3,
        max_length=255,
    )

    recebido_em: datetime

    hash_conteudo: str = Field(
        ...,
        min_length=64,
        max_length=64,
    )

    @field_validator(
        "message_id_externo",
        "assunto",
        "corpo",
        "remetente",
        mode="before",
    )
    @classmethod
    def normalize_text_fields(
        cls,
        value: str | None,
    ) -> str | None:
        if value is None:
            return None

        normalized = value.strip()

        if not normalized:
            return None

        return normalized

    @field_validator("hash_conteudo")
    @classmethod
    def validate_content_hash(
        cls,
        value: str,
    ) -> str:
        normalized = value.strip().lower()

        if len(normalized) != 64:
            raise ValueError(
                "O hash do conteúdo deve possuir 64 caracteres.",
            )

        if any(
            character not in "0123456789abcdef"
            for character in normalized
        ):
            raise ValueError(
                "O hash do conteúdo deve estar em formato hexadecimal.",
            )

        return normalized


class InboxMessageResponse(BaseModel):
    """Representação pública de uma mensagem registrada."""

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    correlation_id: UUID
    canal: CanalEntrada
    origem_processamento: OrigemProcessamento
    status: StatusInboxMessage
    message_id_externo: str | None
    assunto: str
    corpo: str
    remetente: str
    recebido_em: datetime
    hash_conteudo: str
    created_at: datetime
    updated_at: datetime