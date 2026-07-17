from app.modules.operacoes.evidence.models import (
    EvidenceBundle,
)
from app.modules.operacoes.inbox.models import (
    InboxMessage,
)


class BuildEvidenceBundle:
    """
    Constrói o EvidenceBundle a partir
    de uma InboxMessage persistida.
    """

    def execute(
        self,
        message: InboxMessage,
    ) -> EvidenceBundle:
        """
        Cria o Bundle inicial contendo
        comunicação, anexos e metadados.
        """

        return EvidenceBundle(
            message=message,
            attachments=list(message.attachments),
            metadata={
                "canal": message.canal.value,
                "origem": message.origem_processamento.value,
                "message": {
                    "assunto": message.assunto,
                    "corpo": message.corpo,
                    "remetente": message.remetente,
                    "recebido_em": message.recebido_em,
                    "message_id_externo": (
                        message.message_id_externo
                    ),
                },
                "consolidated": {
                    "assunto": message.assunto,
                    "corpo": message.corpo,
                    "remetente": message.remetente,
                },
            },
        )