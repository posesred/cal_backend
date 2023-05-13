import os
import sys
from logging.config import fileConfig

from dotenv import load_dotenv
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from app.shared.base.base_model import ModelMixin as Base

from alembic import context

from app.endpoints.urls import APIPrefix

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
for route in APIPrefix.include:
    try:
        exec(f"from app.api.{route}.models import ModelMixin as Base")
    except ImportError as e:
        print(e)
        # logger.error(f"Route {route} has no tables defined")

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

target_base = Base.metadata

with connectable.connect() as connect:
    context.configure(
        connection=connect, target_metadata=target_base, include_schemas=True
    )

    with context.begin_transaction():
        context.run_migrations()

