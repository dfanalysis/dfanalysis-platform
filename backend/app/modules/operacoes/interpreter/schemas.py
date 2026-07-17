from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field, field_validator


class BusinessExtraction(BaseModel):
    """
    Resultado estruturado extraído de uma comunicação operacional.

    Pode ser produzido por regras, IA, usuário ou combinação
    desses mecanismos.
    """

    empresa_nome: str | None = Field(
        default=None,
        max_length=255,
    )

    empresa_cnpj: str | None = Field(
        default=None,
        min_length=14,
        max_length=14,
    )

    instituicao_nome: str | None = Field(
        default=None,
        max_length=255,
    )

    estabelecimento_nome: str | None = Field(
        default=None,
        max_length=255,
    )

    estabelecimento_cnpj: str | None = Field(
        default=None,
        min_length=14,
        max_length=14,
    )

    tipo_processo: str | None = Field(
        default=None,
        max_length=100,
    )

    competencia: date | None = None

    prazo_envio_nf: date | None = None

    valor: Decimal | None = Field(
        default=None,
        ge=Decimal("0"),
        decimal_places=2,
    )

    descricao_sugerida: str | None = Field(
        default=None,
        max_length=2000,
    )

    medicos: list[str] = Field(
        default_factory=list,
    )

    necessita_faturamento: bool = False

    necessita_emissao_nfse: bool = False

    necessita_repasse: bool = False

    observacoes: list[str] = Field(
        default_factory=list,
    )

    @field_validator(
        "empresa_nome",
        "instituicao_nome",
        "estabelecimento_nome",
        "tipo_processo",
        "descricao_sugerida",
        mode="before",
    )
    @classmethod
    def normalize_optional_text(
        cls,
        value: str | None,
    ) -> str | None:
        if value is None:
            return None

        normalized = value.strip()

        return normalized or None

    @field_validator(
        "empresa_cnpj",
        "estabelecimento_cnpj",
        mode="before",
    )
    @classmethod
    def normalize_cnpj(
        cls,
        value: str | None,
    ) -> str | None:
        if value is None:
            return None

        normalized = "".join(
            character
            for character in value
            if character.isdigit()
        )

        if len(normalized) != 14:
            raise ValueError(
                "O CNPJ deve conter exatamente 14 dígitos.",
            )

        return normalized

    @field_validator("medicos", mode="before")
    @classmethod
    def normalize_medicos(
        cls,
        value: list[str] | None,
    ) -> list[str]:
        if not value:
            return []

        normalized = []

        for medico in value:
            nome = medico.strip()

            if nome and nome not in normalized:
                normalized.append(nome)

        return normalized