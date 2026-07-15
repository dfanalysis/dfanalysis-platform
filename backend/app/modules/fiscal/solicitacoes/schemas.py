from datetime import date, datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator

from app.modules.fiscal.enums import OrigemSolicitacao, StatusSolicitacao


class SolicitacaoEmissaoCreate(BaseModel):
    empresa_id: UUID

    origem: OrigemSolicitacao

    referencia_externa: str | None = Field(
        default=None,
        max_length=255,
    )

    idempotency_key: str | None = Field(
        default=None,
        max_length=255,
    )

    competencia: date

    descricao_servico: str = Field(
        ...,
        min_length=3,
        max_length=2000,
    )

    valor_servico: Decimal = Field(
        ...,
        gt=0,
        max_digits=15,
        decimal_places=2,
    )

    @field_validator(
        "referencia_externa",
        "idempotency_key",
        "descricao_servico",
    )
    @classmethod
    def normalize_text(cls, value: str | None) -> str | None:
        if value is None:
            return None

        normalized_value = value.strip()

        if not normalized_value:
            return None

        return normalized_value


class SolicitacaoEmissaoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    empresa_id: UUID
    correlation_id: UUID
    idempotency_key: str | None
    origem: OrigemSolicitacao
    status: StatusSolicitacao
    referencia_externa: str | None
    competencia: date
    descricao_servico: str
    valor_servico: Decimal
    created_at: datetime
    updated_at: datetime