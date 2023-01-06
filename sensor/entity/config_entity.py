#In this file we are saving all Input of each stage
import os 

FILE_NAME = "sensor.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

class TrainingPipelineConfig:

    def __init__(self):
        #we created artifact folder in current dirwctory for output
        self.artifact_dir = os.path.join(os.getcwd(), "artifact", f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")



    

class DataIngetionConfig:

    def __init__(self, training_pipeline_config : TrainingPipelineConfig):
        try:
            self.database_name = "aps"
            self.collection_name = "sensor"
            self.data_ingetion_dir = os.path.join(training_pipeline_config.artifact_dir, "data_ingetion")
            self.feature_store_dir = os.path.join(self.data_ingestion_dir, "feature_store")
            self.train_file_name = os.path.join(self.data_ingetion_dir, "dataset", TRAIN_FILE_NAME)
            self.test_file_name = os.path.join(self.data_ingetion_dir, "dataset", TEST_FILE_NAME)
        except Exception as e:
            raise SensorException(e, sys)
            
        


    def to_dict() ->dict:
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)





class DataValidationConfig:...
class DataTransformationConfig:...
class ModelTrainerConfig:...
class ModelEvalutionConfig:...
class ModelPusherConfig:...