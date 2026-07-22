from __future__ import annotations

from collections.abc import Callable
from typing import Self

from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.modules.fiscal.rps.infrastructure.repositories.sqlalchemy_rps_repository import (
    SqlAlchemyRpsRepository,
)
from app.modules.fiscal.solicitacoes.repository import (
    SolicitacaoEmissaoRepository,
)
from app.shared.infrastructure.persistence.unit_of_work import (
    AbstractUnitOfWork,
)


SessionFactory = Callable[[], Session]


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    """
    Unit of Work baseado em SQLAlchemy.

    Abre uma sessão por contexto transacional e disponibiliza os
    repositórios que participam do caso de uso.
    """

    def __init__(
        self,
        session_factory: SessionFactory = SessionLocal,
    ) -> None:
        self._session_factory = session_factory
        self.session: Session | None = None

    def __enter__(self) -> Self:
        self.session = self._session_factory()

        self.solicitacoes = SolicitacaoEmissaoRepository(
            self.session,
        )
        self.rps = SqlAlchemyRpsRepository(
            self.session,
        )

        return self

    def commit(self) -> None:
        self._require_session().commit()

    def rollback(self) -> None:
        if self.session is not None:
            self.session.rollback()

    def close(self) -> None:
        if self.session is not None:
            self.session.close()
            self.session = None

    def _require_session(self) -> Session:
        if self.session is None:
            raise RuntimeError(
                "Unit of Work utilizado fora do contexto transacional."
            )

        return self.session