"""Baseline do schema core legado gerenciado pela aplicação.

Revision ID: 20260711_01
Revises:
Create Date: 2026-07-11
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = "20260711_01"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """
    Reproduz o estado legado das tabelas atualmente gerenciadas.

    Esta migration NÃO deve ser executada no banco legado atual.
    No banco existente, utilizaremos somente `alembic stamp`.
    """
    op.execute("CREATE EXTENSION IF NOT EXISTS pgcrypto")
    op.execute("CREATE SCHEMA IF NOT EXISTS core")

    op.create_table(
        "empresa",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("razao_social", sa.String(length=200), nullable=False),
        sa.Column("nome_fantasia", sa.String(length=200), nullable=True),
        sa.Column("cnpj", sa.String(length=14), nullable=False),
        sa.Column("inscricao_municipal", sa.String(length=30), nullable=True),
        sa.Column("inscricao_estadual", sa.String(length=30), nullable=True),
        sa.Column("email", sa.String(length=200), nullable=True),
        sa.Column("telefone", sa.String(length=30), nullable=True),
        sa.Column(
            "ativo",
            sa.Boolean(),
            server_default=sa.text("true"),
            nullable=False,
        ),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name="empresa_pkey"),
        sa.UniqueConstraint("cnpj", name="empresa_cnpj_key"),
        schema="core",
    )
    op.create_index(
        "idx_empresa_ativo",
        "empresa",
        ["ativo"],
        unique=False,
        schema="core",
    )
    op.create_index(
        "idx_empresa_cnpj",
        "empresa",
        ["cnpj"],
        unique=False,
        schema="core",
    )

    op.create_table(
        "perfil",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("nome", sa.String(length=100), nullable=False),
        sa.Column("descricao", sa.Text(), nullable=True),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name="perfil_pkey"),
        sa.UniqueConstraint("nome", name="perfil_nome_key"),
        schema="core",
    )

    op.create_table(
        "usuario",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("empresa_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("nome", sa.String(length=150), nullable=False),
        sa.Column("email", sa.String(length=200), nullable=False),
        sa.Column("senha_hash", sa.Text(), nullable=False),
        sa.Column(
            "ativo",
            sa.Boolean(),
            server_default=sa.text("true"),
            nullable=False,
        ),
        sa.Column("ultimo_login", sa.TIMESTAMP(), nullable=True),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["empresa_id"],
            ["core.empresa.id"],
            name="fk_usuario_empresa",
        ),
        sa.PrimaryKeyConstraint("id", name="usuario_pkey"),
        sa.UniqueConstraint("email", name="usuario_email_key"),
        schema="core",
    )
    op.create_index(
        "idx_usuario_email",
        "usuario",
        ["email"],
        unique=False,
        schema="core",
    )
    op.create_index(
        "idx_usuario_empresa",
        "usuario",
        ["empresa_id"],
        unique=False,
        schema="core",
    )

    op.create_table(
        "usuario_perfil",
        sa.Column(
            "id",
            postgresql.UUID(as_uuid=True),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        sa.Column("usuario_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("perfil_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["perfil_id"],
            ["core.perfil.id"],
            name="fk_usuario_perfil_perfil",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["usuario_id"],
            ["core.usuario.id"],
            name="fk_usuario_perfil_usuario",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name="usuario_perfil_pkey"),
        sa.UniqueConstraint(
            "usuario_id",
            "perfil_id",
            name="uk_usuario_perfil",
        ),
        schema="core",
    )
    op.create_index(
        "idx_usuario_perfil_perfil",
        "usuario_perfil",
        ["perfil_id"],
        unique=False,
        schema="core",
    )
    op.create_index(
        "idx_usuario_perfil_usuario",
        "usuario_perfil",
        ["usuario_id"],
        unique=False,
        schema="core",
    )


def downgrade() -> None:
    """
    Não remove o schema core ou a extensão pgcrypto, pois ambos podem
    conter estruturas externas a esta baseline.
    """
    op.drop_index(
        "idx_usuario_perfil_usuario",
        table_name="usuario_perfil",
        schema="core",
    )
    op.drop_index(
        "idx_usuario_perfil_perfil",
        table_name="usuario_perfil",
        schema="core",
    )
    op.drop_table("usuario_perfil", schema="core")

    op.drop_index(
        "idx_usuario_empresa",
        table_name="usuario",
        schema="core",
    )
    op.drop_index(
        "idx_usuario_email",
        table_name="usuario",
        schema="core",
    )
    op.drop_table("usuario", schema="core")

    op.drop_table("perfil", schema="core")

    op.drop_index(
        "idx_empresa_cnpj",
        table_name="empresa",
        schema="core",
    )
    op.drop_index(
        "idx_empresa_ativo",
        table_name="empresa",
        schema="core",
    )
    op.drop_table("empresa", schema="core")
