from enum import StrEnum


class TipoOperationalCase(StrEnum):
    """
    Tipos de processos operacionais da plataforma.
    """

    FATURAMENTO_HOSPITALAR = "faturamento_hospitalar"
    RECEBIMENTO_FINANCEIRO = "recebimento_financeiro"
    REPASSE_MEDICO = "repasse_medico"
    COMERCIAL = "comercial"
    CONTRATO = "contrato"
    CREDENCIAMENTO = "credenciamento"
    CADASTRO = "cadastro"


class StatusOperationalCase(StrEnum):
    """
    Estados do ciclo de vida do processo.
    """

    ABERTO = "aberto"
    EM_ANALISE = "em_analise"
    EM_EXECUCAO = "em_execucao"
    AGUARDANDO_TERCEIROS = "aguardando_terceiros"
    CONCLUIDO = "concluido"
    CANCELADO = "cancelado"

class EtapaOperationalCase(StrEnum):
    """
    Etapa operacional do processo.
    """

    RECEBIMENTO = "recebimento"

    IMPORTACAO_ANEXOS = "importacao_anexos"

    INTERPRETACAO = "interpretacao"

    CONFERENCIA = "conferencia"

    FATURAMENTO = "faturamento"

    EMISSAO_NFSE = "emissao_nfse"

    ENVIO_NFSE = "envio_nfse"

    AGUARDANDO_RECEBIMENTO = (
        "aguardando_recebimento"
    )

    CONCILIACAO = "conciliacao"

    REPASSE = "repasse"

    DEMONSTRATIVO = "demonstrativo"

    ENCERRAMENTO = "encerramento"