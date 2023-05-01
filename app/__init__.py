"""
author: Sanatjon Burkhanov
github: posesred
"""
import logging
from sqlalchemy_mixins.session import SessionMixin
from fastapi import FastAPI
from fastapi_sqlalchemy.middleware import DBSession, db, DBSessionMiddleware

from app.shared.bases.base_model import ModelMixin
from settings import Config

app = FastAPI()

logging.basicConfig(
    filename='app.log',
    filemode='a'
)
logger = logging.getLogger('app')

app.add_middleware(
    DBSessionMiddleware,
    db_url=f"postgresql+psycopg2://{Config.postgres_connection}",
    engine_args={"pool_size": 100000, "max_overflow": 10000},
)
