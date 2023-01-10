#In this file we are saving all Input of each stage
import os ,sys
from sensor.exception import SensorException
from sensor.logger import logging
from datetime import datetime

FILE_NAME = "sensor.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

class TrainingPipelineConfig:

    def __init__(self):
        """
        Description = This funtion will create folder named as 'artifact' and  store output such as graph, metrics for all entities init
        =================================================================================================================================
        """
        try:
            logging.info("This line will create the folder name as artifact in current directory with proper timestamp and date")
            '''This line will create the folder name as artifact in current directory with proper timestamp and date'''
            self.artifact_dir = os.path.join(os.getcwd(), "artifact", f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        except Exception as e:
            print(e)



    

class DataIngestionConfig:
    def __init__(self, training_pipeline_config : TrainingPipelineConfig):
        """
        We are passing object of class Training_PipelineConfig in each component
        ========================================================================
        """
        try:
            self.database_name = "aps"
            self.collection_name = "sensor"

            
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir, "data_ingetion")
            """ This line will create folder name as 'data_ingestion' and we are joinning it with main folder 'artifact'
                so when we run this function it will create log as "artifact/'date and timestamp'/data_ingestion"
                so this indicates the output of data_ingestion component
            """
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir, "feature_store", FILE_NAME)

            """Here we are creating "feature_store" folder for location of the mongodb database
                we are joining it will "data_ingestion_dir" along with "FILE_NAME"    
            """
            self.train_file_path = os.path.join(self.data_ingestion_dir, "dataset", TRAIN_FILE_NAME)
            """
            Spliting data into two part train and test here in this line we are spliting data for training process
            and creating commman folder for train-test data called "dataset", along with "TRAIN_FILE_NAME"
            """
            self.test_file_path = os.path.join(self.data_ingestion_dir, "dataset", TEST_FILE_NAME)
            """
            Spliting data into two part train and test here in this line we are spliting data for testing process
            and creating commman folder for train-test data called "dataset", along with "TEST_FILE_NAME"
            """
            self.test_size = 0.2
            """
            defining test_size for dataset
            """

        except Exception as e:
            raise SensorException(e, sys)
            
        


    def to_dict(self,) ->dict:
        """
        Description = This function will return all above funtions in dict format
        =========================================================================
        """
        try:
            return self.__dict__
            "self.__dict__ will use to convert funtions into dict "
        except Exception as e:
            raise SensorException(e,sys)





class DataValidationConfig:
    def __init__ (self, training_pipeline_config:TrainingPipelineConfig):
        try:
            self.data_validation_dir = os.path.join(training_pipeline_config.artifact_dir, "data_validation")
            self.report_file_path = os.path.join(self.data_validation_dir, "report.ymal")
            self.missing_threshold = 0.7
            self.base_file_path = os.path.join("/config/workspace/aps_failure_training_set1.csv")
        except Exception as e:
            raise SensorException(e, sys)






class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvalutionConfig:...
class ModelPusherConfig:...