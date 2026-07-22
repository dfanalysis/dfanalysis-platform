from __future__ import annotations

import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.fiscal.rps.application.interfaces.rps_repository import (
    RpsRepository,
)
from app.modules.fiscal.rps.models import Rps


class SqlAlchemyRpsRepository(RpsRepository):
    """Implementação SQLAlchemy do repositório de RPS."""

    def __init__(self, session: Session) -> None:
        self._session = session

    def add(self, rps: Rps) -> Rps:
        self._session.add(rps)
        self._session.flush()

        return rps

    def get_by_id(self, rps_id: uuid.UUID) -> Rps | None:
        statement = select(Rps).where(
            Rps.id == rps_id,
            Rps.deleted_at.is_(None),
        )

        return self._session.scalar(statement)

    def get_by_solicitacao_id(
        self,
        solicitacao_id: uuid.UUID,
    ) -> Rps | None:
        statement = select(Rps).where(
            Rps.solicitacao_id == solicitacao_id,
            Rps.deleted_at.is_(None),
        )

        return self._session.scalar(statement)

    def exists_by_solicitacao_id(
        self,
        solicitacao_id: uuid.UUID,
    ) -> bool:
        statement = (
            select(Rps.id)
            .where(
                Rps.solicitacao_id == solicitacao_id,
                Rps.deleted_at.is_(None),
            )
            .limit(1)
        )

        return self._session.scalar(statement) is not None