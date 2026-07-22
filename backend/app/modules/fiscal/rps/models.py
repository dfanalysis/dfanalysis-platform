from __future__ import annotations

import uuid
from datetime import date
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import (
    Boolean,
    Date,
    Enum as SQLEnum,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
    Text,
    UniqueConstraint,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.db.mixins import (
    SoftDeleteMixin,
    TimestampMixin,
    UUIDPrimaryKeyMixin,
)

from app.modules.fiscal.enums import TipoDocumentoTomador
from .enums import StatusRps

if TYPE_CHECKING:
    from app.modules.empresas.models import Empresa
    from app.modules.fiscal.solicitacoes.models import SolicitacaoEmissao


class Rps(
    UUIDPrimaryKeyMixin,
    TimestampMixin,
    SoftDeleteMixin,
    Base,
):
    """
    Recibo Provisório de Serviços vinculado a uma solicitação de emissão.

    O RPS mantém um snapshot dos dados fiscais utilizados na emissão,
    preservando a rastreabilidade mesmo que os cadastros sejam alterados.
    """

    __tablename__ = "rps"

    __table_args__ = (
        UniqueConstraint(
            "empresa_id",
            "serie",
            "numero",
            name="uq_fiscal_rps_empresa_serie_numero",
        ),
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
        ForeignKey(
            "core.empresa.id",
            ondelete="RESTRICT",
        ),
        nullable=False,
    )

    solicitacao_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "fiscal.solicitacao_emissao.id",
            ondelete="RESTRICT",
        ),
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
        default="RPS",
        server_default="RPS",
    )

    competencia: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    status: Mapped[StatusRps] = mapped_column(
        SQLEnum(
            StatusRps,
            name="status_rps",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        nullable=False,
        default=StatusRps.PENDENTE_ENVIO,
        server_default=StatusRps.PENDENTE_ENVIO.value,
    )

    # Snapshot do tomador

    tomador_tipo_documento: Mapped[TipoDocumentoTomador] = mapped_column(
        SQLEnum(
            TipoDocumentoTomador,
            name="tipo_documento_tomador_rps",
            schema="fiscal",
            values_callable=lambda enum_class: [
                item.value for item in enum_class
            ],
        ),
        nullable=False,
    )

    tomador_documento: Mapped[str] = mapped_column(
        String(14),
        nullable=False,
    )

    tomador_nome: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    medico_nome: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    # Serviço

    valor: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
    )

    descricao: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    # ISSQN

    iss_aliquota: Mapped[Decimal] = mapped_column(
        Numeric(7, 4),
        nullable=False,
        default=Decimal("2.0000"),
        server_default="2.0000",
    )

    iss_valor: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
        default=Decimal("0.00"),
        server_default="0.00",
    )

    iss_retido: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default="false",
    )

    # PIS

    pis_aliquota: Mapped[Decimal] = mapped_column(
        Numeric(7, 4),
        nullable=False,
        default=Decimal("0.6500"),
        server_default="0.6500",
    )

    pis_valor: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
        default=Decimal("0.00"),
        server_default="0.00",
    )

    pis_retido: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default="false",
    )

    # COFINS

    cofins_aliquota: Mapped[Decimal] = mapped_column(
        Numeric(7, 4),
        nullable=False,
        default=Decimal("3.0000"),
        server_default="3.0000",
    )

    cofins_valor: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
        default=Decimal("0.00"),
        server_default="0.00",
    )

    cofins_retido: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default="false",
    )

    # CSLL

    csll_aliquota: Mapped[Decimal] = mapped_column(
        Numeric(7, 4),
        nullable=False,
        default=Decimal("1.0000"),
        server_default="1.0000",
    )

    csll_valor: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
        default=Decimal("0.00"),
        server_default="0.00",
    )

    csll_retido: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default="false",
    )

    # IRRF

    irrf_aliquota: Mapped[Decimal] = mapped_column(
        Numeric(7, 4),
        nullable=False,
        default=Decimal("1.5000"),
        server_default="1.5000",
    )

    irrf_valor: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
        default=Decimal("0.00"),
        server_default="0.00",
    )

    irrf_retido: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default="false",
    )

    # Totais

    total_retencoes: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
        default=Decimal("0.00"),
        server_default="0.00",
    )

    valor_liquido: Mapped[Decimal] = mapped_column(
        Numeric(15, 2),
        nullable=False,
        default=Decimal("0.00"),
        server_default="0.00",
    )

    empresa: Mapped["Empresa"] = relationship()

    solicitacao: Mapped["SolicitacaoEmissao"] = relationship(
        back_populates="rps",
    )