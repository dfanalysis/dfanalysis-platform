from enum import StrEnum


class MetodoInterpretacao(StrEnum):
    """Método utilizado para interpretar uma comunicação."""

    REGRA = "regra"
    IA = "ia"
    USUARIO = "usuario"
    HIBRIDO = "hibrido"
    IMPORTACAO = "importacao"


class StatusInterpretacao(StrEnum):
    """Estados possíveis de uma interpretação."""

    GERADA = "gerada"
    AGUARDANDO_REVISAO = "aguardando_revisao"
    VALIDADA = "validada"
    REJEITADA = "rejeitada"
    SUBSTITUIDA = "substituida"
    ERRO = "erro"