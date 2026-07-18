from logging.config import fileConfig
from typing import Any

from alembic import context
from sqlalchemy import engine_from_config, pool

from app.core.config import settings
from app.db.base import Base

# Importa todos os models registrados na aplicação.
# Esse import é necessário para popular Base.metadata.
import app.db.model_registry  # noqa: F401


config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

config.set_main_option(
    "sqlalchemy.url",
    settings.database_url.render_as_string(
        hide_password=False,
    ),
)

target_metadata = Base.metadata


# Schemas controlados oficialmente pelas migrations da plataforma.
MANAGED_SCHEMAS = frozenset(
    {
        "core",
        "fiscal",
    }
)

# O versionamento do Alembic permanece no schema core.
VERSION_TABLE_SCHEMA = "core"

# Chaves completas das tabelas registradas no metadata.
# Exemplos:
# core.empresa
# core.usuario
# fiscal.solicitacao_emissao
MANAGED_TABLES = frozenset(
    Base.metadata.tables.keys()
)


def include_name(
    name: str | None,
    type_: str,
    parent_names: dict[str, str],
) -> bool:
    """
    Restringe a reflexão do banco aos schemas oficialmente
    administrados pela aplicação.
    """

    if type_ == "schema":
        return name in MANAGED_SCHEMAS

    if type_ == "table":
        schema_name = parent_names.get("schema_name")
        table_key = parent_names.get("schema_qualified_table_name")

        return (
            schema_name in MANAGED_SCHEMAS
            and table_key in MANAGED_TABLES
        )

    return True


def include_object(
    object_: Any,
    name: str | None,
    type_: str,
    reflected: bool,
    compare_to: Any | None,
) -> bool:
    """
    Permite autogenerate somente para objetos pertencentes aos
    schemas e tabelas oficialmente registrados no metadata.
    """

    if type_ == "schema":
        return name in MANAGED_SCHEMAS

    if type_ == "table":
        schema = getattr(object_, "schema", None)
        table_key = getattr(object_, "key", None)

        return (
            schema in MANAGED_SCHEMAS
            and table_key in MANAGED_TABLES
        )

    # Índices, constraints e colunas são permitidos somente quando
    # vinculados às tabelas já filtradas acima.
    return True


def configure_context(**kwargs: object) -> None:
    context.configure(
        target_metadata=target_metadata,
        compare_type=True,
        compare_server_default=True,
        include_schemas=True,
        include_name=include_name,
        include_object=include_object,
        version_table="dfanalysis_alembic_version",
        version_table_schema=VERSION_TABLE_SCHEMA,
        **kwargs,
    )


def run_migrations_offline() -> None:
    configure_context(
        url=settings.database_url.render_as_string(
            hide_password=False,
        ),
        literal_binds=True,
        dialect_opts={
            "paramstyle": "named",
        },
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(
            config.config_ini_section,
            {},
        ),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        configure_context(
            connection=connection,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()