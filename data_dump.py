import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017")

DATABASE_NAME = "aps"  # WE created database for dumping in mongodb
COLLECTION_NAME = "sensor"
DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
 

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")
    

    #Convert Dataframe into json format so that we can dump this record in mongodb
    df.reset_index(drop=True, inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])


    #Inserting in mongodb

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)