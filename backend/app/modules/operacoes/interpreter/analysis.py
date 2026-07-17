from pydantic import BaseModel, Field


class OperationalAnalysis(BaseModel):
    """
    Resultado da análise operacional realizada
    sobre uma comunicação.
    """

    necessita_faturamento: bool = False

    necessita_emissao_nfse: bool = False

    necessita_envio_nfse: bool = False

    necessita_recebimento: bool = False

    necessita_repasse: bool = False

    prioridade: str = "normal"

    confianca: float = Field(
        ge=0,
        le=1,
        default=0.0,
    )

    observacoes: list[str] = Field(
        default_factory=list,
    )