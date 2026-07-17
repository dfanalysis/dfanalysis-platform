from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.operacoes.cases.models import OperationalCase


class OperationalCaseRepository:
    """
    Persistência do Aggregate OperationalCase.
    """

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_id(
        self,
        case_id: UUID,
    ) -> OperationalCase | None:
        statement = select(OperationalCase).where(
            OperationalCase.id == case_id,
        )

        return self.db.scalar(statement)

    def get_by_number(
        self,
        numero: str,
    ) -> OperationalCase | None:
        statement = select(OperationalCase).where(
            OperationalCase.numero == numero,
        )

        return self.db.scalar(statement)

    def list_all(self) -> list[OperationalCase]:
        statement = (
            select(OperationalCase)
            .order_by(
                OperationalCase.created_at.desc(),
            )
        )

        return list(
            self.db.scalars(statement).all()
        )

    def add(
        self,
        case: OperationalCase,
    ) -> OperationalCase:
        self.db.add(case)
        self.db.flush()

        return case