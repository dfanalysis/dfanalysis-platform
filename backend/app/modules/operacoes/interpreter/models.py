from __future__ import annotations

from datetime import datetime
from typing import Any
from uuid import UUID

from sqlalchemy import (
    Boolean,
    DateTime,
    Enum as SQLEnum,
    Float,
    ForeignKey,
    Integer,
    JSON,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID as PostgreSQLUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import (
    SoftDeleteMixin,
    TimestampMixin,
    UUIDPrimaryKeyMixin,
)
from app.modules.operacoes.interpreter.enums import (
    MetodoInterpretacao,
    StatusInterpretacao,
)


class CommunicationInterpretation(
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    SoftDeleteMixin,
    Base,
):
    """
    Interpretação persistida de uma comunicação recebida.

    Preserva o entendimento produzido por regra, IA, usuário
    ou combinação desses mecanismos.
    """

    __tablename__ = "communication_interpretation"
    __table_args__ = {"schema": "operacoes"}

    message_id: Mapped[UUID] = mapped_column(
        PostgreSQLUUID(as_uuid=True),
        ForeignKey(
            "operacoes.inbox_message.id",
            ondelete="CASCADE",
        ),
        nullable=False,
        index=True,
    )

    metodo: Mapped[MetodoInterpretacao] = mapped_column(
        SQLEnum(
            MetodoInterpretacao,
            name="metodo_interpretacao_enum",
            schema="operacoes",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        nullable=False,
        index=True,
    )

    status: Mapped[StatusInterpretacao] = mapped_column(
        SQLEnum(
            StatusInterpretacao,
            name="status_interpretacao_enum",
            schema="operacoes",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        nullable=False,
        default=StatusInterpretacao.GERADA,
        server_default=StatusInterpretacao.GERADA.value,
        index=True,
    )

    confianca: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    necessita_revisao: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True,
        server_default="true",
        index=True,
    )

    resultado: Mapped[dict[str, Any]] = mapped_column(
        JSON,
        nullable=False,
        default=dict,
    )

    engine: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    engine_version: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    prompt_version: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    rule_version: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    sequencia: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
        server_default="1",
    )

    observacoes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    interpretado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    message: Mapped["InboxMessage"] = relationship(
        back_populates="interpretations",
    )


from app.modules.operacoes.inbox.models import InboxMessage  # noqa: E402