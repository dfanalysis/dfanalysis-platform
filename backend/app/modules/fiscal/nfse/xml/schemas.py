from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, Field


class NFSeParty(BaseModel):
    """
    Representa uma parte envolvida na NFS-e.

    Pode ser prestador ou tomador.
    """

    tipo_documento: str
    documento: str
    inscricao_municipal: str | None = None
    nome: str | None = None
    nome_fantasia: str | None = None
    email: str | None = None
    telefone: str | None = None


class NFSeService(BaseModel):
    """
    Dados do serviço prestado.
    """

    codigo_tributacao_nacional: str | None = None
    codigo_tributacao_municipal: str | None = None
    codigo_nbs: str | None = None
    descricao: str | None = None
    informacoes_complementares: str | None = None
    local_prestacao: str | None = None


class NFSeTaxes(BaseModel):
    """
    Informações tributárias e retenções.
    """

    aliquota_iss: Decimal | None = None
    iss_retido: bool = False
    pis_cofins_retidos: bool = False

    valor_iss: Decimal | None = None
    valor_irrf: Decimal | None = None
    valor_csll: Decimal | None = None
    valor_total_retencoes: Decimal | None = None


class NFSeValues(BaseModel):
    """
    Valores financeiros da NFS-e.
    """

    valor_servico: Decimal
    base_calculo: Decimal | None = None
    valor_liquido: Decimal | None = None


class NFSeXMLDocument(BaseModel):
    """
    Representação estruturada de uma NFS-e lida de XML.
    """

    numero_nfse: str
    numero_dps: str | None = None
    serie_dps: str | None = None

    versao_nfse: str | None = None
    versao_dps: str | None = None
    versao_aplicacao: str | None = None

    ambiente: str | None = None
    status: str | None = None

    data_processamento: datetime | None = None
    data_emissao: datetime | None = None
    competencia: date | None = None

    local_emissao: str | None = None
    local_prestacao: str | None = None
    local_incidencia: str | None = None

    prestador: NFSeParty
    tomador: NFSeParty
    servico: NFSeService
    tributos: NFSeTaxes
    valores: NFSeValues

    observacoes: list[str] = Field(
        default_factory=list,
    )