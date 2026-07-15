from app.modules.operacoes.inbox.enums import StatusInboxMessage
from app.modules.operacoes.inbox.exceptions import (
    TransicaoStatusInboxInvalidaError,
)


class InboxDomainService:
    """Regras centrais do domínio de Operações/Inbox."""

    @staticmethod
    def alterar_status(
        status_atual: StatusInboxMessage,
        novo_status: StatusInboxMessage,
    ) -> StatusInboxMessage:
        """Valida e retorna uma transição de status permitida."""

        transicoes_permitidas = {
            StatusInboxMessage.RECEBIDA: {
                StatusInboxMessage.ANEXOS_IMPORTADOS,
                StatusInboxMessage.CLASSIFICADA,
                StatusInboxMessage.AGUARDANDO_REVISAO,
                StatusInboxMessage.ERRO,
                StatusInboxMessage.DESCARTADA,
            },
            StatusInboxMessage.ANEXOS_IMPORTADOS: {
                StatusInboxMessage.CLASSIFICADA,
                StatusInboxMessage.AGUARDANDO_REVISAO,
                StatusInboxMessage.ERRO,
                StatusInboxMessage.DESCARTADA,
            },
            StatusInboxMessage.CLASSIFICADA: {
                StatusInboxMessage.EMPRESA_IDENTIFICADA,
                StatusInboxMessage.AGUARDANDO_REVISAO,
                StatusInboxMessage.ERRO,
                StatusInboxMessage.DESCARTADA,
            },
            StatusInboxMessage.EMPRESA_IDENTIFICADA: {
                StatusInboxMessage.DEMANDA_CRIADA,
                StatusInboxMessage.AGUARDANDO_REVISAO,
                StatusInboxMessage.ERRO,
                StatusInboxMessage.DESCARTADA,
            },
            StatusInboxMessage.AGUARDANDO_REVISAO: {
                StatusInboxMessage.ANEXOS_IMPORTADOS,
                StatusInboxMessage.CLASSIFICADA,
                StatusInboxMessage.EMPRESA_IDENTIFICADA,
                StatusInboxMessage.DEMANDA_CRIADA,
                StatusInboxMessage.ERRO,
                StatusInboxMessage.DESCARTADA,
            },
            StatusInboxMessage.DEMANDA_CRIADA: {
                StatusInboxMessage.PROCESSADA,
                StatusInboxMessage.ERRO,
            },
            StatusInboxMessage.ERRO: {
                StatusInboxMessage.AGUARDANDO_REVISAO,
                StatusInboxMessage.DESCARTADA,
            },
            StatusInboxMessage.PROCESSADA: set(),
            StatusInboxMessage.DESCARTADA: set(),
        }

        status_permitidos = transicoes_permitidas[status_atual]

        if novo_status not in status_permitidos:
            raise TransicaoStatusInboxInvalidaError(
                f"Transição de '{status_atual.value}' "
                f"para '{novo_status.value}' não permitida.",
            )

        return novo_status