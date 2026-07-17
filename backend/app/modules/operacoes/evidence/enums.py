from enum import StrEnum


class TipoEvidencia(StrEnum):
    """Tipos técnicos de evidência suportados pelo pipeline."""

    EMAIL = "email"
    PDF_TEXTUAL = "pdf_textual"
    PDF_DIGITALIZADO = "pdf_digitalizado"
    XML = "xml"
    EXCEL = "excel"
    CSV = "csv"
    IMAGEM = "imagem"
    ZIP = "zip"
    TEXTO = "texto"
    DESCONHECIDO = "desconhecido"


class StatusProcessamentoEvidencia(StrEnum):
    """Estados técnicos do processamento de uma evidência."""

    RECEBIDA = "recebida"
    IDENTIFICADA = "identificada"
    PROCESSANDO = "processando"
    PROCESSADA = "processada"
    COM_ADVERTENCIA = "com_advertencia"
    ERRO = "erro"
    DESCARTADA = "descartada"


class SeveridadeAviso(StrEnum):
    """Severidade de avisos produzidos pelo pipeline."""

    INFORMACAO = "informacao"
    ATENCAO = "atencao"
    CRITICO = "critico"