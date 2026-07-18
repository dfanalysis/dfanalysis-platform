"""create fiscal solicitacao_emissao

Revision ID: c5d193cd907b
Revises: c6329a0f65ce
Create Date: 2026-07-18 16:33:34.067054
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = "c5d193cd907b"
down_revision: Union[str, Sequence[str], None] = "c6329a0f65ce"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


origem_enum = postgresql.ENUM(
    "api",
    "email",
    "erp",
    "n8n",
    "portal",
    "whatsapp",
    "ia",
    "importacao",
    name="origem_solicitacao_enum",
    schema="fiscal",
    create_type=False,
)

status_enum = postgresql.ENUM(
    "recebida",
    "em_validacao",
    "validada",
    "aguardando_processamento",
    "processando",
    "emitida",
    "rejeitada",
    "cancelada",
    "falha",
    name="status_solicitacao_enum",
    schema="fiscal",
    create_type=False,
)


def upgrade() -> None:

    op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")

    op.execute("CREATE SCHEMA IF NOT EXISTS fiscal")

    origem_enum.create(op.get_bind(), checkfirst=True)
    status_enum.create(op.get_bind(), checkfirst=True)

    op.create_table(
        "solicitacao_emissao",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
            server_default=sa.text("gen_random_uuid()"),
        ),
        sa.Column(
            "empresa_id",
            postgresql.UUID(as_uuid=True),
            sa.ForeignKey(
                "core.empresa.id",
                ondelete="RESTRICT",
            ),
            nullable=False,
        ),
        sa.Column(
            "correlation_id",
            postgresql.UUID(as_uuid=True),
            nullable=False,
        ),
        sa.Column(
            "idempotency_key",
            sa.String(255),
            nullable=True,
        ),
        sa.Column(
            "origem",
            origem_enum,
            nullable=False,
        ),
        sa.Column(
            "status",
            status_enum,
            nullable=False,
            server_default="recebida",
        ),
        sa.Column(
            "referencia_externa",
            sa.String(255),
            nullable=True,
        ),
        sa.Column(
            "competencia",
            sa.Date(),
            nullable=False,
        ),
        sa.Column(
            "descricao_servico",
            sa.String(2000),
            nullable=False,
        ),
        sa.Column(
            "valor_servico",
            sa.Numeric(15, 2),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column(
            "deleted_at",
            sa.DateTime(timezone=True),
            nullable=True,
        ),
        sa.UniqueConstraint(
            "correlation_id",
            name="uq_solicitacao_emissao_correlation_id",
        ),
        sa.UniqueConstraint(
            "idempotency_key",
            name="uq_solicitacao_emissao_idempotency_key",
        ),
        schema="fiscal",
    )

    op.create_index(
        "ix_solicitacao_emissao_empresa_id",
        "solicitacao_emissao",
        ["empresa_id"],
        unique=False,
        schema="fiscal",
    )

    op.create_index(
        "ix_solicitacao_emissao_correlation_id",
        "solicitacao_emissao",
        ["correlation_id"],
        unique=True,
        schema="fiscal",
    )

    op.create_index(
        "ix_solicitacao_emissao_status",
        "solicitacao_emissao",
        ["status"],
        unique=False,
        schema="fiscal",
    )

    op.create_index(
        "ix_solicitacao_emissao_competencia",
        "solicitacao_emissao",
        ["competencia"],
        unique=False,
        schema="fiscal",
    )


def downgrade() -> None:

    op.drop_index(
        "ix_solicitacao_emissao_competencia",
        table_name="solicitacao_emissao",
        schema="fiscal",
    )

    op.drop_index(
        "ix_solicitacao_emissao_status",
        table_name="solicitacao_emissao",
        schema="fiscal",
    )

    op.drop_index(
        "ix_solicitacao_emissao_correlation_id",
        table_name="solicitacao_emissao",
        schema="fiscal",
    )

    op.drop_index(
        "ix_solicitacao_emissao_empresa_id",
        table_name="solicitacao_emissao",
        schema="fiscal",
    )

    op.drop_table(
        "solicitacao_emissao",
        schema="fiscal",
    )

    status_enum.drop(op.get_bind(), checkfirst=True)
    origem_enum.drop(op.get_bind(), checkfirst=True)