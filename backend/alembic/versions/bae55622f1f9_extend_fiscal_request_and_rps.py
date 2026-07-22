"""extend fiscal request and rps

Revision ID: bae55622f1f9
Revises: dd30041ed190
Create Date: 2026-07-21 20:32:46.280374
"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = "bae55622f1f9"
down_revision: Union[str, Sequence[str], None] = "dd30041ed190"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


TIPO_DOCUMENTO_TOMADOR = postgresql.ENUM(
    "CPF",
    "CNPJ",
    name="tipo_documento_tomador",
    schema="fiscal",
)

TIPO_DOCUMENTO_TOMADOR_RPS = postgresql.ENUM(
    "CPF",
    "CNPJ",
    name="tipo_documento_tomador_rps",
    schema="fiscal",
)


def _get_status_rps_schema() -> str:
    """
    Localiza o schema real do enum status_rps.

    A migration original do RPS pode ter criado esse tipo no schema
    public ou no schema fiscal. Esta consulta evita assumir incorretamente
    onde o tipo está armazenado.
    """
    bind = op.get_bind()

    schema_name = bind.execute(
        sa.text(
            """
            SELECT namespace.nspname
            FROM pg_type AS type
            JOIN pg_namespace AS namespace
              ON namespace.oid = type.typnamespace
            WHERE type.typname = 'status_rps'
            ORDER BY
                CASE
                    WHEN namespace.nspname = 'fiscal' THEN 1
                    WHEN namespace.nspname = 'public' THEN 2
                    ELSE 3
                END
            LIMIT 1
            """
        )
    ).scalar_one_or_none()

    if schema_name is None:
        raise RuntimeError(
            "O enum PostgreSQL 'status_rps' não foi encontrado."
        )

    return schema_name


def _validate_empty_tables() -> None:
    """
    Impede a criação de colunas obrigatórias sobre registros legados.

    Não é seguro preencher tomador, documento ou nome com dados fictícios.
    Caso existam registros, deve ser criada uma estratégia específica
    de migração e backfill.
    """
    bind = op.get_bind()

    total_rps = bind.execute(
        sa.text("SELECT COUNT(*) FROM fiscal.rps")
    ).scalar_one()

    total_solicitacoes = bind.execute(
        sa.text(
            "SELECT COUNT(*) FROM fiscal.solicitacao_emissao"
        )
    ).scalar_one()

    if total_rps or total_solicitacoes:
        raise RuntimeError(
            "A migration exige as tabelas fiscal.rps e "
            "fiscal.solicitacao_emissao vazias. "
            f"Registros encontrados: rps={total_rps}, "
            f"solicitacoes={total_solicitacoes}."
        )


def upgrade() -> None:
    """Upgrade schema."""
    bind = op.get_bind()

    _validate_empty_tables()

    # Criação explícita dos novos tipos ENUM do PostgreSQL.
    TIPO_DOCUMENTO_TOMADOR.create(bind, checkfirst=True)
    TIPO_DOCUMENTO_TOMADOR_RPS.create(bind, checkfirst=True)

    # O valor precisa ser incluído antes de ser usado como server default.
    # O autocommit é necessário porque o PostgreSQL não permite utilizar
    # imediatamente um novo valor de enum dentro da mesma transação.
    status_rps_schema = _get_status_rps_schema()
    preparer = bind.dialect.identifier_preparer

    qualified_status_rps = (
        f"{preparer.quote(status_rps_schema)}."
        f"{preparer.quote('status_rps')}"
    )

    with op.get_context().autocommit_block():
        op.execute(
            sa.text(
                f"""
                ALTER TYPE {qualified_status_rps}
                ADD VALUE IF NOT EXISTS 'PENDENTE_ENVIO'
                """
            )
        )

    # ------------------------------------------------------------------
    # RPS
    # ------------------------------------------------------------------

    op.add_column(
        "rps",
        sa.Column(
            "tomador_tipo_documento",
            postgresql.ENUM(
                "CPF",
                "CNPJ",
                name="tipo_documento_tomador_rps",
                schema="fiscal",
                create_type=False,
            ),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "tomador_documento",
            sa.String(length=14),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "tomador_nome",
            sa.String(length=255),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "medico_nome",
            sa.String(length=255),
            nullable=True,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "iss_aliquota",
            sa.Numeric(precision=7, scale=4),
            server_default=sa.text("2.0000"),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "iss_valor",
            sa.Numeric(precision=15, scale=2),
            server_default=sa.text("0.00"),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "iss_retido",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "pis_aliquota",
            sa.Numeric(precision=7, scale=4),
            server_default=sa.text("0.6500"),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "pis_valor",
            sa.Numeric(precision=15, scale=2),
            server_default=sa.text("0.00"),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "pis_retido",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "cofins_aliquota",
            sa.Numeric(precision=7, scale=4),
            server_default=sa.text("3.0000"),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "cofins_valor",
            sa.Numeric(precision=15, scale=2),
            server_default=sa.text("0.00"),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "cofins_retido",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "csll_aliquota",
            sa.Numeric(precision=7, scale=4),
            server_default=sa.text("1.0000"),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "csll_valor",
            sa.Numeric(precision=15, scale=2),
            server_default=sa.text("0.00"),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "csll_retido",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "irrf_aliquota",
            sa.Numeric(precision=7, scale=4),
            server_default=sa.text("1.5000"),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "irrf_valor",
            sa.Numeric(precision=15, scale=2),
            server_default=sa.text("0.00"),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "irrf_retido",
            sa.Boolean(),
            server_default=sa.text("false"),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "total_retencoes",
            sa.Numeric(precision=15, scale=2),
            server_default=sa.text("0.00"),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "rps",
        sa.Column(
            "valor_liquido",
            sa.Numeric(precision=15, scale=2),
            server_default=sa.text("0.00"),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.alter_column(
        "rps",
        "serie",
        existing_type=sa.VARCHAR(length=10),
        server_default=sa.text("'RPS'"),
        existing_nullable=False,
        schema="fiscal",
    )

    op.alter_column(
        "rps",
        "status",
        existing_type=postgresql.ENUM(
            "GERADO",
            "PENDENTE_ENVIO",
            "EM_LOTE",
            "ENVIADO",
            "PROCESSADO",
            "REJEITADO",
            "CANCELADO",
            name="status_rps",
            schema=status_rps_schema,
            create_type=False,
        ),
        server_default=sa.text("'PENDENTE_ENVIO'"),
        existing_nullable=False,
        schema="fiscal",
    )

    op.create_unique_constraint(
        "uq_fiscal_rps_empresa_serie_numero",
        "rps",
        ["empresa_id", "serie", "numero"],
        schema="fiscal",
    )

    # Recriação das foreign keys com política explícita de exclusão.
    op.drop_constraint(
        "rps_empresa_id_fkey",
        "rps",
        schema="fiscal",
        type_="foreignkey",
    )

    op.drop_constraint(
        "rps_solicitacao_id_fkey",
        "rps",
        schema="fiscal",
        type_="foreignkey",
    )

    op.create_foreign_key(
        "fk_fiscal_rps_empresa",
        "rps",
        "empresa",
        ["empresa_id"],
        ["id"],
        source_schema="fiscal",
        referent_schema="core",
        ondelete="RESTRICT",
    )

    op.create_foreign_key(
        "fk_fiscal_rps_solicitacao",
        "rps",
        "solicitacao_emissao",
        ["solicitacao_id"],
        ["id"],
        source_schema="fiscal",
        referent_schema="fiscal",
        ondelete="RESTRICT",
    )

    # ------------------------------------------------------------------
    # SOLICITAÇÃO DE EMISSÃO
    # ------------------------------------------------------------------

    op.add_column(
        "solicitacao_emissao",
        sa.Column(
            "tomador_tipo_documento",
            postgresql.ENUM(
                "CPF",
                "CNPJ",
                name="tipo_documento_tomador",
                schema="fiscal",
                create_type=False,
            ),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "solicitacao_emissao",
        sa.Column(
            "tomador_documento",
            sa.String(length=14),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "solicitacao_emissao",
        sa.Column(
            "tomador_nome",
            sa.String(length=255),
            nullable=False,
        ),
        schema="fiscal",
    )

    op.add_column(
        "solicitacao_emissao",
        sa.Column(
            "medico_nome",
            sa.String(length=255),
            nullable=True,
        ),
        schema="fiscal",
    )


def downgrade() -> None:
    """Downgrade schema."""
    bind = op.get_bind()
    status_rps_schema = _get_status_rps_schema()

    # ------------------------------------------------------------------
    # SOLICITAÇÃO DE EMISSÃO
    # ------------------------------------------------------------------

    op.drop_column(
        "solicitacao_emissao",
        "medico_nome",
        schema="fiscal",
    )

    op.drop_column(
        "solicitacao_emissao",
        "tomador_nome",
        schema="fiscal",
    )

    op.drop_column(
        "solicitacao_emissao",
        "tomador_documento",
        schema="fiscal",
    )

    op.drop_column(
        "solicitacao_emissao",
        "tomador_tipo_documento",
        schema="fiscal",
    )

    # ------------------------------------------------------------------
    # RPS
    # ------------------------------------------------------------------

    op.drop_constraint(
        "fk_fiscal_rps_solicitacao",
        "rps",
        schema="fiscal",
        type_="foreignkey",
    )

    op.drop_constraint(
        "fk_fiscal_rps_empresa",
        "rps",
        schema="fiscal",
        type_="foreignkey",
    )

    op.create_foreign_key(
        "rps_solicitacao_id_fkey",
        "rps",
        "solicitacao_emissao",
        ["solicitacao_id"],
        ["id"],
        source_schema="fiscal",
        referent_schema="fiscal",
    )

    op.create_foreign_key(
        "rps_empresa_id_fkey",
        "rps",
        "empresa",
        ["empresa_id"],
        ["id"],
        source_schema="fiscal",
        referent_schema="core",
    )

    op.drop_constraint(
        "uq_fiscal_rps_empresa_serie_numero",
        "rps",
        schema="fiscal",
        type_="unique",
    )

    op.execute(
        sa.text(
            """
            UPDATE fiscal.rps
            SET status = 'GERADO'
            WHERE status = 'PENDENTE_ENVIO'
            """
        )
    )

    op.alter_column(
        "rps",
        "status",
        existing_type=postgresql.ENUM(
            "GERADO",
            "PENDENTE_ENVIO",
            "EM_LOTE",
            "ENVIADO",
            "PROCESSADO",
            "REJEITADO",
            "CANCELADO",
            name="status_rps",
            schema=status_rps_schema,
            create_type=False,
        ),
        server_default=None,
        existing_nullable=False,
        schema="fiscal",
    )

    op.alter_column(
        "rps",
        "serie",
        existing_type=sa.VARCHAR(length=10),
        server_default=None,
        existing_nullable=False,
        schema="fiscal",
    )

    op.drop_column("rps", "valor_liquido", schema="fiscal")
    op.drop_column("rps", "total_retencoes", schema="fiscal")

    op.drop_column("rps", "irrf_retido", schema="fiscal")
    op.drop_column("rps", "irrf_valor", schema="fiscal")
    op.drop_column("rps", "irrf_aliquota", schema="fiscal")

    op.drop_column("rps", "csll_retido", schema="fiscal")
    op.drop_column("rps", "csll_valor", schema="fiscal")
    op.drop_column("rps", "csll_aliquota", schema="fiscal")

    op.drop_column("rps", "cofins_retido", schema="fiscal")
    op.drop_column("rps", "cofins_valor", schema="fiscal")
    op.drop_column("rps", "cofins_aliquota", schema="fiscal")

    op.drop_column("rps", "pis_retido", schema="fiscal")
    op.drop_column("rps", "pis_valor", schema="fiscal")
    op.drop_column("rps", "pis_aliquota", schema="fiscal")

    op.drop_column("rps", "iss_retido", schema="fiscal")
    op.drop_column("rps", "iss_valor", schema="fiscal")
    op.drop_column("rps", "iss_aliquota", schema="fiscal")

    op.drop_column("rps", "medico_nome", schema="fiscal")
    op.drop_column("rps", "tomador_nome", schema="fiscal")
    op.drop_column("rps", "tomador_documento", schema="fiscal")
    op.drop_column(
        "rps",
        "tomador_tipo_documento",
        schema="fiscal",
    )

    TIPO_DOCUMENTO_TOMADOR_RPS.drop(bind, checkfirst=True)
    TIPO_DOCUMENTO_TOMADOR.drop(bind, checkfirst=True)

    # O valor PENDENTE_ENVIO permanece no enum status_rps.
    #
    # O PostgreSQL não oferece remoção direta e segura de valores de enum.
    # Recriar o tipo durante um downgrade aumenta significativamente o risco
    # operacional e não é necessário para restaurar a estrutura das tabelas.