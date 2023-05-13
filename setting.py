"""
Author Sanatjon Burkhanov
github: posesred
this is the base settings that gets the enviroment we are using
if it does not find a set enviroment it will have default values
it gets the info from our .env file
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    postgress_connection: str = os.getenv('POSTGRES_CONNECTION')
    # goes into the env class and takes the postgress connection var
    remote_url: str = os.getenv('REMOTE_URL', '')
    # goest ot the env file getst he remote url varible however I dont get the  '' after
