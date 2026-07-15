from enum import StrEnum


class CanalEntrada(StrEnum):
    """Canais suportados para entrada de comunicações."""

    EMAIL = "email"
    WHATSAPP = "whatsapp"
    API = "api"
    WEBHOOK = "webhook"
    UPLOAD_MANUAL = "upload_manual"
    ERP = "erp"
    OUTRO = "outro"


class StatusInboxMessage(StrEnum):
    """Estados possíveis de uma mensagem recebida."""

    RECEBIDA = "recebida"
    ANEXOS_IMPORTADOS = "anexos_importados"
    CLASSIFICADA = "classificada"
    EMPRESA_IDENTIFICADA = "empresa_identificada"
    AGUARDANDO_REVISAO = "aguardando_revisao"
    DEMANDA_CRIADA = "demanda_criada"
    PROCESSADA = "processada"
    ERRO = "erro"
    DESCARTADA = "descartada"


class OrigemProcessamento(StrEnum):
    """Origem responsável pelo ingresso da mensagem na plataforma."""

    INTEGRACAO = "integracao"
    USUARIO = "usuario"
    AGENTE_IA = "agente_ia"
    WORKFLOW = "workflow"
    SISTEMA_EXTERNO = "sistema_externo"


class StatusInboxAttachment(StrEnum):
    """Estados possíveis de um anexo recebido."""

    RECEBIDO = "recebido"
    ARMAZENADO = "armazenado"
    VALIDADO = "validado"
    CLASSIFICADO = "classificado"
    AGUARDANDO_REVISAO = "aguardando_revisao"
    ERRO = "erro"
    DESCARTADO = "descartado"


class ProvedorArmazenamento(StrEnum):
    """Provedores suportados para armazenamento de anexos."""

    LOCAL = "local"
    S3 = "s3"
    MINIO = "minio"
    SUPABASE = "supabase"
    GOOGLE_DRIVE = "google_drive"
    ONEDRIVE = "onedrive"
    OUTRO = "outro"