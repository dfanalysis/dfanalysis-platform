"""add indexes to rps

Revision ID: dd30041ed190
Revises: b3897de9f11d
Create Date: 2026-07-21

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = "dd30041ed190"
down_revision: Union[str, Sequence[str], None] = "b3897de9f11d"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create indexes for fiscal.rps."""

    op.create_index(
        "ix_fiscal_rps_competencia",
        "rps",
        ["competencia"],
        unique=False,
        schema="fiscal",
    )

    op.create_index(
        "ix_fiscal_rps_empresa_id",
        "rps",
        ["empresa_id"],
        unique=False,
        schema="fiscal",
    )

    op.create_index(
        "ix_fiscal_rps_numero",
        "rps",
        ["numero"],
        unique=False,
        schema="fiscal",
    )

    op.create_index(
        "ix_fiscal_rps_status",
        "rps",
        ["status"],
        unique=False,
        schema="fiscal",
    )


def downgrade() -> None:
    """Remove indexes from fiscal.rps."""

    op.drop_index(
        "ix_fiscal_rps_status",
        table_name="rps",
        schema="fiscal",
    )

    op.drop_index(
        "ix_fiscal_rps_numero",
        table_name="rps",
        schema="fiscal",
    )

    op.drop_index(
        "ix_fiscal_rps_empresa_id",
        table_name="rps",
        schema="fiscal",
    )

    op.drop_index(
        "ix_fiscal_rps_competencia",
        table_name="rps",
        schema="fiscal",
    )