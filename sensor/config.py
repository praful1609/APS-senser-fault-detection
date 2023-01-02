import pymongo
import pandas as pd
import json
from dataclasses import dataclass


#Provide the mongodb localhost url to connect python to mongdb.


class EnvironmentVariable:
client = pymongo.MongoClient("mongodb://localhost:27017")