from __future__ import annotations

from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy import (
    BigInteger,
    DateTime,
    Enum as SQLEnum,
    ForeignKey,
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
from app.modules.operacoes.inbox.enums import (
    CanalEntrada,
    OrigemProcessamento,
    ProvedorArmazenamento,
    StatusInboxAttachment,
    StatusInboxMessage,
)


class InboxMessage(
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    SoftDeleteMixin,
    Base,
):
    """
    Aggregate Root do domínio Operações.

    Representa qualquer comunicação recebida
    pela Plataforma DF Analysis IA.
    """

    __tablename__ = "inbox_message"
    __table_args__ = {"schema": "operacoes"}

    correlation_id: Mapped[UUID] = mapped_column(
        PostgreSQLUUID(as_uuid=True),
        default=uuid4,
        nullable=False,
        unique=True,
        index=True,
    )

    canal: Mapped[CanalEntrada] = mapped_column(
        SQLEnum(
            CanalEntrada,
            name="canal_entrada_enum",
            schema="operacoes",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        nullable=False,
    )

    origem_processamento: Mapped[OrigemProcessamento] = mapped_column(
        SQLEnum(
            OrigemProcessamento,
            name="origem_processamento_enum",
            schema="operacoes",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        nullable=False,
    )

    status: Mapped[StatusInboxMessage] = mapped_column(
        SQLEnum(
            StatusInboxMessage,
            name="status_inbox_enum",
            schema="operacoes",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        nullable=False,
        default=StatusInboxMessage.RECEBIDA,
        server_default=StatusInboxMessage.RECEBIDA.value,
        index=True,
    )

    message_id_externo: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
        index=True,
    )

    assunto: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    corpo: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    remetente: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    recebido_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        index=True,
    )

    hash_conteudo: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        unique=True,
        index=True,
    )

    attachments: Mapped[list["InboxAttachment"]] = relationship(
        back_populates="message",
        cascade="all, delete-orphan",
        lazy="selectin",
    )

    interpretations: Mapped[
        list["CommunicationInterpretation"]
    ] = relationship(
        back_populates="message",
        cascade="all, delete-orphan",
        lazy="selectin",
        order_by="CommunicationInterpretation.sequencia",
    )


class InboxAttachment(
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    SoftDeleteMixin,
    Base,
):
    """
    Entidade pertencente ao Aggregate InboxMessage.

    Representa um arquivo recebido juntamente com a comunicação.
    """

    __tablename__ = "inbox_attachment"
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

    nome_original: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )

    mime_type: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    tamanho_bytes: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
    )

    hash_sha256: Mapped[str] = mapped_column(
        String(64),
        nullable=False,
        index=True,
    )

    provedor: Mapped[ProvedorArmazenamento] = mapped_column(
        SQLEnum(
            ProvedorArmazenamento,
            name="provedor_armazenamento_enum",
            schema="operacoes",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        nullable=False,
    )

    storage_key: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
    )

    status: Mapped[StatusInboxAttachment] = mapped_column(
        SQLEnum(
            StatusInboxAttachment,
            name="status_inbox_attachment_enum",
            schema="operacoes",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        nullable=False,
        default=StatusInboxAttachment.RECEBIDO,
        server_default=StatusInboxAttachment.RECEBIDO.value,
        index=True,
    )

    message: Mapped["InboxMessage"] = relationship(
        back_populates="attachments",
    )


from app.modules.operacoes.interpreter.models import (  # noqa: E402
    CommunicationInterpretation,
)