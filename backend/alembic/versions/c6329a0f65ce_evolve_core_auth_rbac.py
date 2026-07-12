"""evolve core auth rbac

Revision ID: c6329a0f65ce
Revises: 20260711_01
Create Date: 2026-07-11 23:40:42.561394
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


revision: str = "c6329a0f65ce"
down_revision: Union[str, Sequence[str], None] = "20260711_01"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


SCHEMA = "core"
LEGACY_TIMEZONE = "America/Sao_Paulo"


def upgrade() -> None:
    """Evolui autenticação, perfis e RBAC sem perda de dados."""

    # =========================================================================
    # RBAC: permissões e relacionamento perfil-permissão
    # =========================================================================
    op.create_table(
        "permissao",
        sa.Column("codigo", sa.String(length=150), nullable=False),
        sa.Column("nome", sa.String(length=150), nullable=False),
        sa.Column("descricao", sa.String(length=500), nullable=True),
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
            "is_active",
            sa.Boolean(),
            server_default=sa.text("true"),
            nullable=False,
        ),
        sa.PrimaryKeyConstraint("id", name="pk_permissao"),
        sa.UniqueConstraint("codigo", name="uq_permissao_codigo"),
        schema=SCHEMA,
    )

    op.create_table(
        "perfil_permissao",
        sa.Column("perfil_id", sa.UUID(), nullable=False),
        sa.Column("permissao_id", sa.UUID(), nullable=False),
        sa.ForeignKeyConstraint(
            ["perfil_id"],
            [f"{SCHEMA}.perfil.id"],
            name="fk_perfil_permissao_perfil",
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["permissao_id"],
            [f"{SCHEMA}.permissao.id"],
            name="fk_perfil_permissao_permissao",
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint(
            "perfil_id",
            "permissao_id",
            name="pk_perfil_permissao",
        ),
        schema=SCHEMA,
    )

    # =========================================================================
    # Empresa
    # =========================================================================
    op.alter_column(
        "empresa",
        "ativo",
        new_column_name="is_active",
        existing_type=sa.Boolean(),
        existing_nullable=False,
        schema=SCHEMA,
    )

    op.add_column(
        "empresa",
        sa.Column(
            "deleted_at",
            sa.DateTime(timezone=True),
            nullable=True,
        ),
        schema=SCHEMA,
    )

    op.alter_column(
        "empresa",
        "razao_social",
        existing_type=sa.VARCHAR(length=200),
        type_=sa.String(length=255),
        existing_nullable=False,
        schema=SCHEMA,
    )

    op.alter_column(
        "empresa",
        "nome_fantasia",
        existing_type=sa.VARCHAR(length=200),
        type_=sa.String(length=255),
        existing_nullable=True,
        schema=SCHEMA,
    )

    op.alter_column(
        "empresa",
        "created_at",
        existing_type=postgresql.TIMESTAMP(),
        type_=sa.DateTime(timezone=True),
        existing_nullable=False,
        existing_server_default=sa.text("now()"),
        postgresql_using=(
            f"created_at AT TIME ZONE '{LEGACY_TIMEZONE}'"
        ),
        schema=SCHEMA,
    )

    op.alter_column(
        "empresa",
        "updated_at",
        existing_type=postgresql.TIMESTAMP(),
        type_=sa.DateTime(timezone=True),
        existing_nullable=False,
        existing_server_default=sa.text("now()"),
        postgresql_using=(
            f"updated_at AT TIME ZONE '{LEGACY_TIMEZONE}'"
        ),
        schema=SCHEMA,
    )

    op.drop_index(
        "idx_empresa_ativo",
        table_name="empresa",
        schema=SCHEMA,
    )

    op.drop_index(
        "idx_empresa_cnpj",
        table_name="empresa",
        schema=SCHEMA,
    )

    # =========================================================================
    # Perfil
    # =========================================================================
    op.add_column(
        "perfil",
        sa.Column("codigo", sa.String(length=100), nullable=True),
        schema=SCHEMA,
    )

    op.add_column(
        "perfil",
        sa.Column(
            "is_system",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
        ),
        schema=SCHEMA,
    )

    op.add_column(
        "perfil",
        sa.Column(
            "is_active",
            sa.Boolean(),
            server_default=sa.text("true"),
            nullable=False,
        ),
        schema=SCHEMA,
    )

    op.execute(
        sa.text(
            "UPDATE core.perfil "
            "SET "
            "codigo = CASE nome "
            "WHEN 'Administrador' THEN 'administrador' "
            "WHEN 'API' THEN 'api' "
            "WHEN 'Comercial' THEN 'comercial' "
            "WHEN 'Financeiro' THEN 'financeiro' "
            "WHEN 'Fiscal' THEN 'fiscal' "
            "WHEN 'IA' THEN 'ia' "
            "WHEN 'Operador' THEN 'operador' "
            "ELSE 'legacy-' || id::text "
            "END, "
            "is_system = CASE "
            "WHEN nome IN ("
            "'Administrador', 'API', 'Comercial', 'Financeiro', "
            "'Fiscal', 'IA', 'Operador'"
            ") THEN true "
            "ELSE false "
            "END"
        )
    )

    op.alter_column(
        "perfil",
        "codigo",
        existing_type=sa.String(length=100),
        nullable=False,
        schema=SCHEMA,
    )

    op.alter_column(
        "perfil",
        "nome",
        existing_type=sa.VARCHAR(length=100),
        type_=sa.String(length=150),
        existing_nullable=False,
        schema=SCHEMA,
    )

    op.alter_column(
        "perfil",
        "descricao",
        existing_type=sa.TEXT(),
        type_=sa.String(length=500),
        existing_nullable=True,
        schema=SCHEMA,
    )

    op.alter_column(
        "perfil",
        "created_at",
        existing_type=postgresql.TIMESTAMP(),
        type_=sa.DateTime(timezone=True),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
        postgresql_using=f"created_at AT TIME ZONE '{LEGACY_TIMEZONE}'",
        schema=SCHEMA,
    )

    op.alter_column(
        "perfil",
        "updated_at",
        existing_type=postgresql.TIMESTAMP(),
        type_=sa.DateTime(timezone=True),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
        postgresql_using=f"updated_at AT TIME ZONE '{LEGACY_TIMEZONE}'",
        schema=SCHEMA,
    )

    op.drop_constraint(
        "perfil_nome_key",
        "perfil",
        schema=SCHEMA,
        type_="unique",
    )

    op.create_unique_constraint(
        "uq_perfil_codigo",
        "perfil",
        ["codigo"],
        schema=SCHEMA,
    )

    # =========================================================================
    # Usuário
    # =========================================================================
    op.alter_column(
        "usuario",
        "senha_hash",
        new_column_name="password_hash",
        existing_type=sa.TEXT(),
        existing_nullable=False,
        schema=SCHEMA,
    )

    op.alter_column(
        "usuario",
        "ultimo_login",
        new_column_name="last_login_at",
        existing_type=postgresql.TIMESTAMP(),
        existing_nullable=True,
        schema=SCHEMA,
    )

    op.alter_column(
        "usuario",
        "ativo",
        new_column_name="is_active",
        existing_type=sa.Boolean(),
        existing_nullable=False,
        schema=SCHEMA,
    )

    op.add_column(
        "usuario",
        sa.Column("deleted_at", sa.DateTime(timezone=True), nullable=True),
        schema=SCHEMA,
    )

    op.alter_column(
        "usuario",
        "password_hash",
        existing_type=sa.TEXT(),
        type_=sa.String(length=255),
        existing_nullable=False,
        schema=SCHEMA,
    )

    op.alter_column(
        "usuario",
        "nome",
        existing_type=sa.VARCHAR(length=150),
        type_=sa.String(length=255),
        existing_nullable=False,
        schema=SCHEMA,
    )

    op.alter_column(
        "usuario",
        "email",
        existing_type=sa.VARCHAR(length=200),
        type_=sa.String(length=255),
        existing_nullable=False,
        schema=SCHEMA,
    )

    op.alter_column(
        "usuario",
        "last_login_at",
        existing_type=postgresql.TIMESTAMP(),
        type_=sa.DateTime(timezone=True),
        existing_nullable=True,
        postgresql_using=f"last_login_at AT TIME ZONE '{LEGACY_TIMEZONE}'",
        schema=SCHEMA,
    )

    op.alter_column(
        "usuario",
        "created_at",
        existing_type=postgresql.TIMESTAMP(),
        type_=sa.DateTime(timezone=True),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
        postgresql_using=f"created_at AT TIME ZONE '{LEGACY_TIMEZONE}'",
        schema=SCHEMA,
    )

    op.alter_column(
        "usuario",
        "updated_at",
        existing_type=postgresql.TIMESTAMP(),
        type_=sa.DateTime(timezone=True),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
        postgresql_using=f"updated_at AT TIME ZONE '{LEGACY_TIMEZONE}'",
        schema=SCHEMA,
    )

    op.drop_index(
        "idx_usuario_email",
        table_name="usuario",
        schema=SCHEMA,
    )

    op.drop_index(
        "idx_usuario_empresa",
        table_name="usuario",
        schema=SCHEMA,
    )

    op.create_index(
        "ix_core_usuario_empresa_id",
        "usuario",
        ["empresa_id"],
        unique=False,
        schema=SCHEMA,
    )

    op.drop_constraint(
        "fk_usuario_empresa",
        "usuario",
        schema=SCHEMA,
        type_="foreignkey",
    )

    op.create_foreign_key(
        "fk_usuario_empresa",
        "usuario",
        "empresa",
        ["empresa_id"],
        ["id"],
        source_schema=SCHEMA,
        referent_schema=SCHEMA,
        ondelete="RESTRICT",
    )

    # =========================================================================
    # Usuário-Perfil
    # =========================================================================
    op.drop_index(
        "idx_usuario_perfil_usuario",
        table_name="usuario_perfil",
        schema=SCHEMA,
    )

    op.drop_constraint(
        "uk_usuario_perfil",
        "usuario_perfil",
        schema=SCHEMA,
        type_="unique",
    )

    op.drop_constraint(
        "usuario_perfil_pkey",
        "usuario_perfil",
        schema=SCHEMA,
        type_="primary",
    )

    op.drop_column(
        "usuario_perfil",
        "id",
        schema=SCHEMA,
    )

    op.drop_column(
        "usuario_perfil",
        "created_at",
        schema=SCHEMA,
    )

    op.create_primary_key(
        "pk_usuario_perfil",
        "usuario_perfil",
        ["usuario_id", "perfil_id"],
        schema=SCHEMA,
    )


def downgrade() -> None:
    """Restaura a estrutura anterior à evolução de RBAC."""

    # =========================================================================
    # Usuário-Perfil
    # =========================================================================
    op.drop_constraint(
        "pk_usuario_perfil",
        "usuario_perfil",
        schema=SCHEMA,
        type_="primary",
    )

    op.add_column(
        "usuario_perfil",
        sa.Column(
            "id",
            sa.UUID(),
            server_default=sa.text("gen_random_uuid()"),
            nullable=False,
        ),
        schema=SCHEMA,
    )

    op.add_column(
        "usuario_perfil",
        sa.Column(
            "created_at",
            postgresql.TIMESTAMP(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
        schema=SCHEMA,
    )

    op.create_primary_key(
        "usuario_perfil_pkey",
        "usuario_perfil",
        ["id"],
        schema=SCHEMA,
    )

    op.create_unique_constraint(
        "uk_usuario_perfil",
        "usuario_perfil",
        ["usuario_id", "perfil_id"],
        schema=SCHEMA,
    )

    op.create_index(
        "idx_usuario_perfil_usuario",
        "usuario_perfil",
        ["usuario_id"],
        unique=False,
        schema=SCHEMA,
    )

    # =========================================================================
    # Usuário
    # =========================================================================
    op.drop_constraint(
        "fk_usuario_empresa",
        "usuario",
        schema=SCHEMA,
        type_="foreignkey",
    )

    op.create_foreign_key(
        "fk_usuario_empresa",
        "usuario",
        "empresa",
        ["empresa_id"],
        ["id"],
        source_schema=SCHEMA,
        referent_schema=SCHEMA,
    )

    op.drop_index(
        "ix_core_usuario_empresa_id",
        table_name="usuario",
        schema=SCHEMA,
    )

    op.create_index(
        "idx_usuario_empresa",
        "usuario",
        ["empresa_id"],
        unique=False,
        schema=SCHEMA,
    )

    op.create_index(
        "idx_usuario_email",
        "usuario",
        ["email"],
        unique=False,
        schema=SCHEMA,
    )

    op.alter_column(
        "usuario",
        "updated_at",
        existing_type=sa.DateTime(timezone=True),
        type_=postgresql.TIMESTAMP(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
        postgresql_using=f"updated_at AT TIME ZONE '{LEGACY_TIMEZONE}'",
        schema=SCHEMA,
    )

    op.alter_column(
        "usuario",
        "created_at",
        existing_type=sa.DateTime(timezone=True),
        type_=postgresql.TIMESTAMP(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
        postgresql_using=f"created_at AT TIME ZONE '{LEGACY_TIMEZONE}'",
        schema=SCHEMA,
    )

    op.alter_column(
        "usuario",
        "last_login_at",
        existing_type=sa.DateTime(timezone=True),
        type_=postgresql.TIMESTAMP(),
        existing_nullable=True,
        postgresql_using=f"last_login_at AT TIME ZONE '{LEGACY_TIMEZONE}'",
        schema=SCHEMA,
    )

    op.alter_column(
        "usuario",
        "email",
        existing_type=sa.String(length=255),
        type_=sa.VARCHAR(length=200),
        existing_nullable=False,
        schema=SCHEMA,
    )

    op.alter_column(
        "usuario",
        "nome",
        existing_type=sa.String(length=255),
        type_=sa.VARCHAR(length=150),
        existing_nullable=False,
        schema=SCHEMA,
    )

    op.alter_column(
        "usuario",
        "password_hash",
        existing_type=sa.String(length=255),
        type_=sa.TEXT(),
        existing_nullable=False,
        schema=SCHEMA,
    )

    op.drop_column("usuario", "deleted_at", schema=SCHEMA)

    op.alter_column(
        "usuario",
        "is_active",
        new_column_name="ativo",
        existing_type=sa.Boolean(),
        existing_nullable=False,
        schema=SCHEMA,
    )

    op.alter_column(
        "usuario",
        "last_login_at",
        new_column_name="ultimo_login",
        existing_type=postgresql.TIMESTAMP(),
        existing_nullable=True,
        schema=SCHEMA,
    )

    op.alter_column(
        "usuario",
        "password_hash",
        new_column_name="senha_hash",
        existing_type=sa.TEXT(),
        existing_nullable=False,
        schema=SCHEMA,
    )

    # =========================================================================
    # Perfil
    # =========================================================================
    op.drop_constraint(
        "uq_perfil_codigo",
        "perfil",
        schema=SCHEMA,
        type_="unique",
    )

    op.create_unique_constraint(
        "perfil_nome_key",
        "perfil",
        ["nome"],
        schema=SCHEMA,
    )

    op.alter_column(
        "perfil",
        "updated_at",
        existing_type=sa.DateTime(timezone=True),
        type_=postgresql.TIMESTAMP(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
        postgresql_using=f"updated_at AT TIME ZONE '{LEGACY_TIMEZONE}'",
        schema=SCHEMA,
    )

    op.alter_column(
        "perfil",
        "created_at",
        existing_type=sa.DateTime(timezone=True),
        type_=postgresql.TIMESTAMP(),
        existing_nullable=False,
        existing_server_default=sa.text("CURRENT_TIMESTAMP"),
        postgresql_using=f"created_at AT TIME ZONE '{LEGACY_TIMEZONE}'",
        schema=SCHEMA,
    )

    op.alter_column(
        "perfil",
        "descricao",
        existing_type=sa.String(length=500),
        type_=sa.TEXT(),
        existing_nullable=True,
        schema=SCHEMA,
    )

    op.alter_column(
        "perfil",
        "nome",
        existing_type=sa.String(length=150),
        type_=sa.VARCHAR(length=100),
        existing_nullable=False,
        schema=SCHEMA,
    )

    op.drop_column("perfil", "is_active", schema=SCHEMA)
    op.drop_column("perfil", "is_system", schema=SCHEMA)
    op.drop_column("perfil", "codigo", schema=SCHEMA)

    # =========================================================================
    # Empresa
    # =========================================================================
    op.create_index(
        "idx_empresa_cnpj",
        "empresa",
        ["cnpj"],
        unique=False,
        schema=SCHEMA,
    )

    op.create_index(
        "idx_empresa_ativo",
        "empresa",
        ["is_active"],
        unique=False,
        schema=SCHEMA,
    )

    op.alter_column(
        "empresa",
        "updated_at",
        existing_type=sa.DateTime(timezone=True),
        type_=postgresql.TIMESTAMP(),
        existing_nullable=False,
        existing_server_default=sa.text("now()"),
        postgresql_using=f"updated_at AT TIME ZONE '{LEGACY_TIMEZONE}'",
        schema=SCHEMA,
    )

    op.alter_column(
        "empresa",
        "created_at",
        existing_type=sa.DateTime(timezone=True),
        type_=postgresql.TIMESTAMP(),
        existing_nullable=False,
        existing_server_default=sa.text("now()"),
        postgresql_using=f"created_at AT TIME ZONE '{LEGACY_TIMEZONE}'",
        schema=SCHEMA,
    )

    op.alter_column(
        "empresa",
        "nome_fantasia",
        existing_type=sa.String(length=255),
        type_=sa.VARCHAR(length=200),
        existing_nullable=True,
        schema=SCHEMA,
    )

    op.alter_column(
        "empresa",
        "razao_social",
        existing_type=sa.String(length=255),
        type_=sa.VARCHAR(length=200),
        existing_nullable=False,
        schema=SCHEMA,
    )

    op.drop_column("empresa", "deleted_at", schema=SCHEMA)

    op.alter_column(
        "empresa",
        "is_active",
        new_column_name="ativo",
        existing_type=sa.Boolean(),
        existing_nullable=False,
        schema=SCHEMA,
    )

    # =========================================================================
    # RBAC
    # =========================================================================
    op.drop_table("perfil_permissao", schema=SCHEMA)
    op.drop_table("permissao", schema=SCHEMA)
