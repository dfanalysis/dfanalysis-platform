from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Boolean, Column, ForeignKey, Index, String, Table
from sqlalchemy.dialects.postgresql import UUID as PostgreSQLUUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import ActiveMixin, TimestampMixin, UUIDPrimaryKeyMixin

if TYPE_CHECKING:
    from app.modules.usuarios.models import Usuario


usuario_perfil = Table(
    "usuario_perfil",
    Base.metadata,
    Column(
        "usuario_id",
        PostgreSQLUUID(as_uuid=True),
        ForeignKey("core.usuario.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "perfil_id",
        PostgreSQLUUID(as_uuid=True),
        ForeignKey("core.perfil.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    schema="core",
)

Index(
    "idx_usuario_perfil_perfil",
    usuario_perfil.c.perfil_id,
)


perfil_permissao = Table(
    "perfil_permissao",
    Base.metadata,
    Column(
        "perfil_id",
        PostgreSQLUUID(as_uuid=True),
        ForeignKey("core.perfil.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "permissao_id",
        PostgreSQLUUID(as_uuid=True),
        ForeignKey("core.permissao.id", ondelete="CASCADE"),
        primary_key=True,
        nullable=False,
    ),
    schema="core",
)


class Perfil(UUIDPrimaryKeyMixin, TimestampMixin, ActiveMixin, Base):
    __tablename__ = "perfil"
    __table_args__ = {"schema": "core"}

    codigo: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    nome: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    descricao: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    is_system: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        server_default="false",
        nullable=False,
    )

    usuarios: Mapped[list["Usuario"]] = relationship(
        secondary=usuario_perfil,
        back_populates="perfis",
        lazy="selectin",
    )

    permissoes: Mapped[list["Permissao"]] = relationship(
        secondary=perfil_permissao,
        back_populates="perfis",
        lazy="selectin",
    )


class Permissao(UUIDPrimaryKeyMixin, TimestampMixin, ActiveMixin, Base):
    __tablename__ = "permissao"
    __table_args__ = {"schema": "core"}

    codigo: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
    )

    nome: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    descricao: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    perfis: Mapped[list["Perfil"]] = relationship(
        secondary=perfil_permissao,
        back_populates="permissoes",
        lazy="selectin",
    )
