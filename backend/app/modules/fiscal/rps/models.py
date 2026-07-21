from __future__ import annotations

import uuid
from datetime import date
from decimal import Decimal

from sqlalchemy import (
    Date,
    Enum,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import (
    SoftDeleteMixin,
    TimestampMixin,
    UUIDPrimaryKeyMixin,
)

from .enums import StatusRps


class Rps(
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    SoftDeleteMixin,
    Base,
):
    __tablename__ = "rps"

    __table_args__ = (
        Index(
            "ix_fiscal_rps_empresa_id",
            "empresa_id",
        ),
        Index(
            "ix_fiscal_rps_competencia",
            "competencia",
        ),
        Index(
            "ix_fiscal_rps_status",
            "status",
        ),
        Index(
            "ix_fiscal_rps_numero",
            "numero",
        ),
        {
            "schema": "fiscal",
        },
    )

    empresa_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("core.empresa.id"),
        nullable=False,
    )

    solicitacao_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("fiscal.solicitacao_emissao.id"),
        nullable=False,
        unique=True,
    )

    numero: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    serie: Mapped[str] = mapped_column(
        String(10),
        nullable=False,
    )

    competencia: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    status: Mapped[StatusRps] = mapped_column(
        Enum(
            StatusRps,
            name="status_rps",
        ),
        nullable=False,
        default=StatusRps.GERADO,
    )

    valor: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
    )

    descricao: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    empresa = relationship(
        "Empresa",
    )

    solicitacao = relationship(
        "SolicitacaoEmissao",
        back_populates="rps",
    )