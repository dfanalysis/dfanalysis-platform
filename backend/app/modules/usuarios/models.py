from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PostgreSQLUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import ActiveMixin, SoftDeleteMixin, TimestampMixin, UUIDPrimaryKeyMixin
from app.modules.auth.models import usuario_perfil

if TYPE_CHECKING:
    from app.modules.auth.models import Perfil
    from app.modules.empresas.models import Empresa


class Usuario(
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    ActiveMixin,
    SoftDeleteMixin,
    Base,
):
    __tablename__ = "usuario"
    __table_args__ = {"schema": "core"}

    empresa_id: Mapped[UUID] = mapped_column(
        PostgreSQLUUID(as_uuid=True),
        ForeignKey("core.empresa.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    nome: Mapped[str] = mapped_column(String(255), nullable=False)

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    last_login_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    empresa: Mapped["Empresa"] = relationship(
        back_populates="usuarios",
        lazy="joined",
    )

    perfis: Mapped[list["Perfil"]] = relationship(
        secondary=usuario_perfil,
        back_populates="usuarios",
        lazy="selectin",
    )
