import pandas as pd
import pymongo  
from sensor.config import mongo_client
from sensor.logger import logging
from sensor.exception import SensorException


def get_collection_as_dataframe(DATABASE_NAME:str, COLLECTION_NAME:str) -> pd.DataFrame:
    """
    Description: This function return collection as dataframe

    DATABASE_NAME = DATABASE_NAME
    COLLECTION_NAME = COLLECTION_NAME
    ==========================================================
    return Pandas dataframe of collection
    """
    try: 
        logging.info(f"reading dataframe from database {DATABASE_NAME} and collection {COLLECTION_NAME}")
        df = pd.DataFrame(list( mongo_client[DATABASE_NAME][COLLECTION_NAME].find()))
        logging.info(f"found columns {df.columns}")

        #  there will be one unneccessary column will get added called '_id' by mongodb so we need to drop it
        logging.info("droping column '_id' ")
        if "_id" in df.columns:
            df = df.drop("_id", axis = 1)
        logging.info(f"Rows and columns in df: {df.shape}")

    except Exception as e:
        raise SensorException(e, sys)
