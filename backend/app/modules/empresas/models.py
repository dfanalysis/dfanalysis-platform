from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import (
    ActiveMixin,
    SoftDeleteMixin,
    TimestampMixin,
    UUIDPrimaryKeyMixin,
)

if TYPE_CHECKING:
    from app.modules.usuarios.models import Usuario
    from app.modules.fiscal.solicitacoes.models import SolicitacaoEmissao


class Empresa(
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    ActiveMixin,
    SoftDeleteMixin,
    Base,
):
    """
    Empresa/tenant cadastrada na Plataforma DF Analysis IA.

    Centraliza os dados institucionais, fiscais e de contato necessários
    para os módulos da plataforma, incluindo o emissor de NFS-e.
    """

    __tablename__ = "empresa"

    __table_args__ = (
        CheckConstraint(
            "char_length(cnpj) = 14",
            name="empresa_cnpj_length",
        ),
        {"schema": "core"},
    )

    razao_social: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    nome_fantasia: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    cnpj: Mapped[str] = mapped_column(
        String(14),
        unique=True,
        nullable=False,
    )

    inscricao_municipal: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    inscricao_estadual: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    email: Mapped[str | None] = mapped_column(
        String(200),
        nullable=True,
    )

    telefone: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    usuarios: Mapped[list["Usuario"]] = relationship(
        back_populates="empresa",
        lazy="selectin",
    )

    solicitacoes_emissao: Mapped[list["SolicitacaoEmissao"]] = relationship(
    back_populates="empresa",
    lazy="selectin",
)
