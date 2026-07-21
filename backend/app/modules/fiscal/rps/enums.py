from enum import Enum


class StatusRps(str, Enum):
    GERADO = "GERADO"
    EM_LOTE = "EM_LOTE"
    ENVIADO = "ENVIADO"
    PROCESSADO = "PROCESSADO"
    REJEITADO = "REJEITADO"
    CANCELADO = "CANCELADO"