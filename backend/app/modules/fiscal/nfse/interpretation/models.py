from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal


@dataclass(frozen=True, slots=True)
class NFSeParty:
    """
    Representa uma parte envolvida no documento fiscal.

    Pode representar o prestador ou o tomador do serviço.
    """

    tipo_documento: str
    documento: str
    inscricao_municipal: str | None = None
    nome: str | None = None
    nome_fantasia: str | None = None
    email: str | None = None
    telefone: str | None = None


@dataclass(frozen=True, slots=True)
class NFSeService:
    """
    Representa o serviço descrito na NFS-e.
    """

    codigo_tributacao_nacional: str | None = None
    codigo_tributacao_municipal: str | None = None
    codigo_nbs: str | None = None
    descricao: str | None = None
    informacoes_complementares: str | None = None
    local_prestacao: str | None = None


@dataclass(frozen=True, slots=True)
class NFSeValues:
    """
    Representa os valores financeiros do documento fiscal.
    """

    valor_servico: Decimal
    base_calculo: Decimal | None = None
    valor_liquido: Decimal | None = None


@dataclass(frozen=True, slots=True)
class NFSeTaxes:
    """
    Representa a tributação e as retenções da NFS-e.
    """

    aliquota_iss: Decimal | None = None
    iss_retido: bool = False
    pis_cofins_retidos: bool = False
    valor_iss: Decimal | None = None
    valor_irrf: Decimal | None = None
    valor_csll: Decimal | None = None
    valor_total_retencoes: Decimal | None = None


@dataclass(frozen=True, slots=True)
class NFSeIdentification:
    """
    Identificação funcional do documento fiscal.
    """

    numero_nfse: str
    numero_dps: str | None = None
    serie_dps: str | None = None
    data_emissao: datetime | None = None
    competencia: date | None = None
    ambiente: str | None = None
    status: str | None = None


@dataclass(frozen=True, slots=True)
class NFSeMetadata:
    """
    Metadados técnicos e de rastreabilidade do documento.
    """

    versao_nfse: str | None = None
    versao_dps: str | None = None
    versao_aplicacao: str | None = None
    data_processamento: datetime | None = None
    local_emissao: str | None = None
    local_prestacao: str | None = None
    local_incidencia: str | None = None
    observacoes: tuple[str, ...] = field(
        default_factory=tuple,
    )


@dataclass(frozen=True, slots=True)
class NFSeBusinessDocument:
    """
    Representação normalizada de uma NFS-e no domínio fiscal.

    Este modelo não depende de XML, banco de dados, FastAPI ou de um
    provedor específico de emissão.
    """

    identificacao: NFSeIdentification
    prestador: NFSeParty
    tomador: NFSeParty
    servico: NFSeService
    valores: NFSeValues
    tributos: NFSeTaxes
    metadados: NFSeMetadata