from sqlalchemy.orm import Session

from app.modules.operacoes.inbox.models import InboxMessage
from app.modules.operacoes.inbox.repository import (
    InboxMessageRepository,
)
from app.modules.operacoes.inbox.schemas import (
    InboxMessageCreate,
)


class CreateInboxMessage:
    """Caso de uso responsável por registrar uma comunicação recebida."""

    def __init__(self, db: Session) -> None:
        self.db = db
        self.repository = InboxMessageRepository(db)

    def execute(
        self,
        payload: InboxMessageCreate,
    ) -> InboxMessage:
        """Cria uma nova mensagem de Inbox."""

        if payload.message_id_externo:
            existente = self.repository.get_by_external_message_id(
                payload.message_id_externo,
            )

            if existente is not None:
                return existente

        existente = self.repository.get_by_content_hash(
            payload.hash_conteudo,
        )

        if existente is not None:
            return existente

        message = InboxMessage(
            canal=payload.canal,
            origem_processamento=payload.origem_processamento,
            message_id_externo=payload.message_id_externo,
            assunto=payload.assunto,
            corpo=payload.corpo,
            remetente=payload.remetente,
            recebido_em=payload.recebido_em,
            hash_conteudo=payload.hash_conteudo,
        )

        return self.repository.add(message)