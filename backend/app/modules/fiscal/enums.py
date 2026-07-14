from enum import Enum


class OrigemSolicitacao(str, Enum):
    """Origem da solicitação de emissão."""

    API = "api"
    EMAIL = "email"
    ERP = "erp"
    N8N = "n8n"
    PORTAL = "portal"
    WHATSAPP = "whatsapp"
    IA = "ia"
    IMPORTACAO = "importacao"


class StatusSolicitacao(str, Enum):
    """Situação atual da solicitação de emissão."""

    RECEBIDA = "recebida"
    EM_VALIDACAO = "em_validacao"
    VALIDADA = "validada"
    AGUARDANDO_PROCESSAMENTO = "aguardando_processamento"
    PROCESSANDO = "processando"
    EMITIDA = "emitida"
    REJEITADA = "rejeitada"
    CANCELADA = "cancelada"
    FALHA = "falha"