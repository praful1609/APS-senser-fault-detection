#In this file we are saving collection related code

import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os


#Provide the mongodb localhost url to connect python to mongdb.

@dataclass
class EnvironmentVariable:
    mongo_db_url : str = os.getenv("MONGO_DB_URL")


env_var = EnvironmentVariable()
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)   