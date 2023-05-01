"""
Author: Sanatjon Burkhanov
Github: posesred
"""
import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    postgres_connection: str = os.getenv('POSTGRES_CONNECTION')
    remote_url: str = os.getenv('REMOTE_URL', '')
