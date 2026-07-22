from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.modules.fiscal.enums import StatusSolicitacao
from app.modules.fiscal.solicitacoes.models import SolicitacaoEmissao


class SolicitacaoEmissaoRepository:
    """Operações de persistência das solicitações de emissão."""

    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_id(
        self,
        solicitacao_id: UUID,
    ) -> SolicitacaoEmissao | None:
        statement = select(SolicitacaoEmissao).where(
            SolicitacaoEmissao.id == solicitacao_id,
            SolicitacaoEmissao.deleted_at.is_(None),
        )

        return self.db.scalar(statement)

    def get_by_correlation_id(
        self,
        correlation_id: UUID,
    ) -> SolicitacaoEmissao | None:
        statement = select(SolicitacaoEmissao).where(
            SolicitacaoEmissao.correlation_id == correlation_id,
        )

        return self.db.scalar(statement)

    def get_by_idempotency_key(
        self,
        idempotency_key: str,
    ) -> SolicitacaoEmissao | None:
        statement = select(SolicitacaoEmissao).where(
            SolicitacaoEmissao.idempotency_key == idempotency_key,
        )

        return self.db.scalar(statement)

    def list_by_empresa(
        self,
        empresa_id: UUID,
        *,
        status: StatusSolicitacao | None = None,
    ) -> list[SolicitacaoEmissao]:
        statement = select(SolicitacaoEmissao).where(
            SolicitacaoEmissao.empresa_id == empresa_id,
            SolicitacaoEmissao.deleted_at.is_(None),
        )

        if status is not None:
            statement = statement.where(
                SolicitacaoEmissao.status == status,
            )

        statement = statement.order_by(
            SolicitacaoEmissao.created_at.desc(),
        )

        return list(self.db.scalars(statement).all())

    def add(
        self,
        solicitacao: SolicitacaoEmissao,
    ) -> SolicitacaoEmissao:
        self.db.add(solicitacao)
        self.db.flush()

        return solicitacao

    def update(
        self,
        solicitacao: SolicitacaoEmissao,
    ) -> SolicitacaoEmissao:
        """
        Atualiza uma solicitação já persistida.

        O objeto recebido deve estar associado à sessão atual.
        """

        self.db.flush()

        return solicitacao