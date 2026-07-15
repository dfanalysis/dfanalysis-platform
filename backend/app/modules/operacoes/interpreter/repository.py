from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.modules.operacoes.interpreter.models import (
    CommunicationInterpretation,
)


class CommunicationInterpretationRepository:
    """Persistência das interpretações de comunicações."""

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_id(
        self,
        interpretation_id: UUID,
    ) -> CommunicationInterpretation | None:
        statement = select(CommunicationInterpretation).where(
            CommunicationInterpretation.id == interpretation_id,
        )

        return self.db.scalar(statement)

    def list_by_message_id(
        self,
        message_id: UUID,
    ) -> list[CommunicationInterpretation]:
        statement = (
            select(CommunicationInterpretation)
            .where(
                CommunicationInterpretation.message_id == message_id,
            )
            .order_by(
                CommunicationInterpretation.sequencia.asc(),
            )
        )

        return list(self.db.scalars(statement).all())

    def get_latest_by_message_id(
        self,
        message_id: UUID,
    ) -> CommunicationInterpretation | None:
        statement = (
            select(CommunicationInterpretation)
            .where(
                CommunicationInterpretation.message_id == message_id,
            )
            .order_by(
                CommunicationInterpretation.sequencia.desc(),
            )
            .limit(1)
        )

        return self.db.scalar(statement)

    def get_next_sequence(
        self,
        message_id: UUID,
    ) -> int:
        statement = select(
            func.coalesce(
                func.max(CommunicationInterpretation.sequencia),
                0,
            )
        ).where(
            CommunicationInterpretation.message_id == message_id,
        )

        current_sequence = self.db.scalar(statement) or 0

        return current_sequence + 1

    def add(
        self,
        interpretation: CommunicationInterpretation,
    ) -> CommunicationInterpretation:
        self.db.add(interpretation)
        self.db.flush()

        return interpretation