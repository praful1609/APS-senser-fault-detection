from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe
from sensor.entity import config_entity
from sensor.entity.config_entity import DataIngetionConfig
from datetime import datetime
import sys, os
from sensor.components import DataIngestion


if __name__=="__main__":
     try:
          training_pipeline_config = config_entity.TrainingPipelineConfig()
          data_ingetion_config = config.entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
          print(data_ingetion_config.to_dict())
          data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
          print(data_ingestion.initiate_data_ingestion())
     except Exception as e:
          print(e)

