from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.operacoes.inbox.models import InboxMessage


class InboxMessageRepository:
    """Operações de persistência do Aggregate InboxMessage."""

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_id(
        self,
        message_id: UUID,
    ) -> InboxMessage | None:
        statement = select(InboxMessage).where(
            InboxMessage.id == message_id,
        )

        return self.db.scalar(statement)

    def get_by_correlation_id(
        self,
        correlation_id: UUID,
    ) -> InboxMessage | None:
        statement = select(InboxMessage).where(
            InboxMessage.correlation_id == correlation_id,
        )

        return self.db.scalar(statement)

    def get_by_external_message_id(
        self,
        message_id_externo: str,
    ) -> InboxMessage | None:
        statement = select(InboxMessage).where(
            InboxMessage.message_id_externo == message_id_externo,
        )

        return self.db.scalar(statement)

    def get_by_content_hash(
        self,
        hash_conteudo: str,
    ) -> InboxMessage | None:
        statement = select(InboxMessage).where(
            InboxMessage.hash_conteudo == hash_conteudo,
        )

        return self.db.scalar(statement)

    def add(
        self,
        message: InboxMessage,
    ) -> InboxMessage:
        self.db.add(message)
        self.db.flush()

        return message