from __future__ import annotations

from datetime import datetime
from typing import Any
from uuid import UUID

from pydantic import BaseModel, Field


class AIDocumentContext(BaseModel):
    """
    Representação segura e serializável de um documento processado.
    """

    evidence_id: UUID
    tipo: str
    status: str
    parser: str
    parser_version: str | None = None
    conteudo: dict[str, Any] = Field(
        default_factory=dict,
    )
    texto_extraido: str | None = None


class AIWarningContext(BaseModel):
    """
    Advertência operacional enviada ao mecanismo de IA.
    """

    codigo: str
    mensagem: str
    severidade: str
    evidence_id: UUID | None = None


class AICommunicationContext(BaseModel):
    """
    Contexto operacional controlado enviado ao provedor de IA.

    Objetos SQLAlchemy e metadados internos não são enviados
    diretamente ao modelo.
    """

    correlation_id: UUID

    canal: str | None = None
    origem: str | None = None

    assunto: str | None = None
    corpo: str | None = None
    remetente: str | None = None
    recebido_em: datetime | None = None

    operation_type: str | None = None

    consolidated: dict[str, Any] = Field(
        default_factory=dict,
    )

    documents: list[AIDocumentContext] = Field(
        default_factory=list,
    )

    warnings: list[AIWarningContext] = Field(
        default_factory=list,
    )


class AIOperationalResponse(BaseModel):
    """
    Contrato validado da interpretação operacional produzida pela IA.
    """

    empresa_nome: str | None = None
    empresa_cnpj: str | None = None

    instituicao_nome: str | None = None
    estabelecimento_nome: str | None = None
    estabelecimento_cnpj: str | None = None

    tipo_processo: str | None = None

    competencia: str | None = None
    prazo_envio_nf: str | None = None

    valor: str | int | float | None = None
    descricao_sugerida: str | None = None

    medicos: list[str] = Field(
        default_factory=list,
    )

    necessita_faturamento: bool = False
    necessita_emissao_nfse: bool = False
    necessita_envio_nfse: bool = False
    necessita_recebimento: bool = False
    necessita_repasse: bool = False

    prioridade: str = "normal"

    confianca: float = Field(
        default=0.0,
        ge=0,
        le=1,
    )

    observacoes: list[str] = Field(
        default_factory=list,
    )