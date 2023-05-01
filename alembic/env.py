import os
import sys
from logging.config import fileConfig

from anyio.streams import file
from dotenv import load_dotenv

from app.api.operation.models import OperationHistory
from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = OperationHistory.metadata


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    load_dotenv(os.path.join(BASE_DIR, ".env"))
    sys.path.append(BASE_DIR)
    config = context.config
    url = f'postgresql+psycopg2://{os.environ["POSTGRES_CONNECTION"]}'
    config.set_main_option("sqlalchemy.url", url)
    alembic_config = config.get_section(config.config_ini_section)
    connectable = engine_from_config(
        alembic_config, prefix="sqlalchemy.", poolclass=pool.NullPool
    )

    with connectable.connect() as connect:
        context.configure(
            connection=connect, target_metadata=target_metadata, include_schemas=True
        )

        with context.begin_transaction():
            context.run_migrations()

run_migrations_online()