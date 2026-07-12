from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from app.core.config import settings
from app.db.base import Base
import app.db.model_registry  # noqa: F401


config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

config.set_main_option(
    "sqlalchemy.url",
    settings.database_url.render_as_string(hide_password=False),
)

target_metadata = Base.metadata

MANAGED_SCHEMA = "core"
MANAGED_TABLES = frozenset(Base.metadata.tables.keys())


def include_name(name: str | None, type_: str, parent_names: dict[str, str]) -> bool:
    """Restringe a reflexão ao schema oficial da plataforma."""
    if type_ == "schema":
        return name == MANAGED_SCHEMA

    if type_ == "table":
        return parent_names.get("schema_name") == MANAGED_SCHEMA

    return True


def include_object(
    object_: object,
    name: str | None,
    type_: str,
    reflected: bool,
    compare_to: object | None,
) -> bool:
    """
    Permite autogenerate exclusivamente para tabelas presentes
    no metadata oficial da aplicação.
    """
    if type_ == "schema":
        return name == MANAGED_SCHEMA

    if type_ == "table":
        schema = getattr(object_, "schema", None)
        key = getattr(object_, "key", None)

        return schema == MANAGED_SCHEMA and key in MANAGED_TABLES

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
        version_table_schema=MANAGED_SCHEMA,
        **kwargs,
    )


def run_migrations_offline() -> None:
    configure_context(
        url=settings.database_url.render_as_string(hide_password=False),
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        configure_context(connection=connection)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
