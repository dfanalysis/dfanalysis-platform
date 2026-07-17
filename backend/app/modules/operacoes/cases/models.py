from __future__ import annotations

from uuid import UUID

from sqlalchemy import Enum as SQLEnum, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PostgreSQLUUID
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.db.mixins import (
    SoftDeleteMixin,
    TimestampMixin,
    UUIDPrimaryKeyMixin,
)
from app.modules.operacoes.cases.enums import (
    EtapaOperationalCase,
    StatusOperationalCase,
    TipoOperationalCase,
)


class OperationalCase(
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    SoftDeleteMixin,
    Base,
):
    """
    Aggregate Root do Kernel da Plataforma DF Analysis IA.

    Representa um processo operacional do início ao fim.
    """

    __tablename__ = "operational_case"
    __table_args__ = {"schema": "operacoes"}

    numero: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
        unique=True,
        index=True,
    )

    tipo: Mapped[TipoOperationalCase] = mapped_column(
        SQLEnum(
            TipoOperationalCase,
            name="tipo_operational_case_enum",
            schema="operacoes",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        nullable=False,
        index=True,
    )

    status: Mapped[StatusOperationalCase] = mapped_column(
        SQLEnum(
            StatusOperationalCase,
            name="status_operational_case_enum",
            schema="operacoes",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        nullable=False,
        default=StatusOperationalCase.ABERTO,
        server_default=StatusOperationalCase.ABERTO.value,
        index=True,
    )

    etapa: Mapped[EtapaOperationalCase] = mapped_column(
        SQLEnum(
            EtapaOperationalCase,
            name="etapa_operational_case_enum",
            schema="operacoes",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        nullable=False,
        default=EtapaOperationalCase.RECEBIMENTO,
        server_default=EtapaOperationalCase.RECEBIMENTO.value,
        index=True,
    )

    communication_id: Mapped[UUID | None] = mapped_column(
        PostgreSQLUUID(as_uuid=True),
        ForeignKey(
            "operacoes.inbox_message.id",
            ondelete="SET NULL",
        ),
        nullable=True,
        index=True,
    )