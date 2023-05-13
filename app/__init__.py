"""
author: Sanatjon Burkhanov
github: posesred
this sets up a fastapi module and sets up a basic configuration for logging
"""
import logging
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi.middleware.cors import CORSMiddleware

from setting import Config
from shared.base.base_model import ModelMixin

app = FastAPI()
origins = [
    'http://localhost:3000',
    'http://localhost',
    'http://127.0.0.1',
    'http://127.0.0,1:3000'
]

logging.basicConfig(
    filename='app.log',
    filemode='a'
)
logger = logging.getLogger('app')

app.add_middleware(DBSessionMiddleware, db_url=f'postgresql+psycopg2://{Config.postgress_connection}')

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


