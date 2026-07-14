from __future__ import annotations

from datetime import date
from decimal import Decimal
from typing import TYPE_CHECKING
from uuid import UUID, uuid4

from sqlalchemy import Date, Enum as SQLEnum, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID as PostgreSQLUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import SoftDeleteMixin, TimestampMixin, UUIDPrimaryKeyMixin
from app.modules.fiscal.enums import OrigemSolicitacao, StatusSolicitacao

if TYPE_CHECKING:
    from app.modules.empresas.models import Empresa


class SolicitacaoEmissao(
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    SoftDeleteMixin,
    Base,
):
    """
    Aggregate Root do processo de emissão fiscal.

    Representa a solicitação recebida pela plataforma antes da geração
    do documento provisório e da eventual autorização da NFS-e.
    """

    __tablename__ = "solicitacao_emissao"
    __table_args__ = {"schema": "fiscal"}

    empresa_id: Mapped[UUID] = mapped_column(
        PostgreSQLUUID(as_uuid=True),
        ForeignKey("core.empresa.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    correlation_id: Mapped[UUID] = mapped_column(
        PostgreSQLUUID(as_uuid=True),
        default=uuid4,
        nullable=False,
        unique=True,
        index=True,
    )

    idempotency_key: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        unique=True,
    )

    origem: Mapped[OrigemSolicitacao] = mapped_column(
        SQLEnum(
            OrigemSolicitacao,
            name="origem_solicitacao_enum",
            schema="fiscal",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        nullable=False,
    )

    status: Mapped[StatusSolicitacao] = mapped_column(
        SQLEnum(
            StatusSolicitacao,
            name="status_solicitacao_enum",
            schema="fiscal",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        default=StatusSolicitacao.RECEBIDA,
        server_default=StatusSolicitacao.RECEBIDA.value,
        nullable=False,
        index=True,
    )

    referencia_externa: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    competencia: Mapped[date] = mapped_column(
        Date,
        nullable=False,
        index=True,
    )

    descricao_servico: Mapped[str] = mapped_column(
        String(2000),
        nullable=False,
    )

    valor_servico: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
    )

    empresa: Mapped["Empresa"] = relationship(
        back_populates="solicitacoes_emissao",
        lazy="joined",
    )