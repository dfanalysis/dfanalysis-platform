"""create rps table

Revision ID: b3897de9f11d
Revises: c5d193cd907b
Create Date: 2026-07-21 11:33:40.957851

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b3897de9f11d"
down_revision: Union[str, Sequence[str], None] = "c5d193cd907b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "rps",
        sa.Column("empresa_id", sa.UUID(), nullable=False),
        sa.Column("solicitacao_id", sa.UUID(), nullable=False),
        sa.Column("numero", sa.Integer(), nullable=False),
        sa.Column("serie", sa.String(length=10), nullable=False),
        sa.Column("competencia", sa.Date(), nullable=False),
        sa.Column(
            "status",
            sa.Enum(
                "GERADO",
                "EM_LOTE",
                "ENVIADO",
                "PROCESSADO",
                "REJEITADO",
                "CANCELADO",
                name="status_rps",
            ),
            nullable=False,
        ),
        sa.Column(
            "valor",
            sa.Numeric(precision=15, scale=2),
            nullable=False,
        ),
        sa.Column(
            "descricao",
            sa.Text(),
            nullable=False,
        ),
        sa.Column(
            "id",
            sa.UUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "deleted_at",
            sa.DateTime(timezone=True),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["empresa_id"],
            ["core.empresa.id"],
        ),
        sa.ForeignKeyConstraint(
            ["solicitacao_id"],
            ["fiscal.solicitacao_emissao.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("solicitacao_id"),
        schema="fiscal",
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_table(
        "rps",
        schema="fiscal",
    )