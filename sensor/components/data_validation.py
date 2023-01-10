from sensor.entity import artifact_entity
from sensor.entity import config_entity
from sensor.logger import logging
from sensor.exception import SensorException
import os,sys
from scipy.stats import ks_2samp
import pandas as pd
from typing import Optional
from sensor import utils
import numpy as np

class DataValidation:
    
    def __init__(self,data_validation_config:config_entity.DataValidationConfig,
    data_ingestion_artifact:artifact_entity.DataIngestionArtifact):
        try:
            logging.info(f"{'>>'*20} Data Validation {'<<'*20}")
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
            self.validation_error=dict()
        except Exception as e:
            raise SensorException(e, sys)
        
    def drop_missing_value_columns(self,df:pd.DataFrame,report_key_name:str)->Optional[pd.DataFrame]:
        """
        Description: This function will drop the columns which have missing value more than specific threshold

        df: Accept a pandas Dataframe
        threshold: Percentage criteria to drop a column
        =======================================================================================================
        return Pandas Dataframe if atleast a single column in availble after missing column drop else None
        """
        try:
            threshold = self.DataValidationConfig.missing_threshold
            null_report = df.isna().sum()/df.shape[0]

            #selecting column name which contains null_values
            drop_column_names = null_report[null_report>threshold].index
            self.validation_error[report_key_name]=drop_column_names
            df.drop(list(drop_column_names), axis=1, inplace=True)

            # Return None if no column left
            if len(df.columns)==0:
                return None
            return df
        except exception as e:
            raise SensorException(e,sys)


    def is_required_column_present(self,base_df:pd.DataFrame, current_df:pd.DataFrame, report_key_name:str)->bool:
        try:
            drift_report = dict()
            base_columns = base_df.columns
            current_columns = current_df.columns

            missing_columns = []
            for base_column in base_columns:
                if base_column not in current_columns:
                    missing_columns.append(base_column)

            if len(missing_columns)>0:
                self.validation_error[report_key_name]=missing_columns
                return False
            return True
        
        except Exception as e:
            raise SensorException(e, sys)
    
    def data_drift(self, base_df:pd.DataFrame, current_df:pd.DataFrame,report_key_name:str):
        try:
            drift_report = dict()  
            base_columns = base_df.columns
            current_columns = current_df.columns

            for base_column in base_columns:
                base_data, current_data = base_df[base_column], current_df[base_column]
                #null hypothesis is that column data drawn from same distribution
                same_distrubution = ks_2samp(base_data, current_data)

                if same_distrubution.pvalue > 0.05:
                    # We are accepting null hypothesis
                    drift_report[base_column]={
                        "pvalues":same_distrubution.pvalue,
                        "same_distrubution":True
                    }
                else:
                    drift_report[base_column]={
                        "pvalues":same_distrubution.pvalue,
                        "same_distrubution":False
                    }
                    # Different distribution

            self.validation_error[report_key_name]=drift_report
        except Exception as e:
            raise SensorException(e, sys)


    
    def initiate_data_validation(self) ->artifact_entity.DataValidationArtifact:
        try:
            base_df = pd.read_csv(self.data_validation_config.base_file_path)
            #base_df has na as null
            base_df.replace({"na", np.NAN}, inplace=True)

            base_df = self.drop_missing_value_columns(df=base_df, report_key_name="missing_value_within_base_dataset")

            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            train__df = self.drop_missing_value_columns(df=train__df, report_key_name="missing_value_within_train_dataset")
            test__df = self.drop_missing_value_columns(df=test__df, report_key_name="missing_value_within_test_dataset")
            
            logging.info(f"Is all required columns present in train df")
            train_df_columns_status = self.is_required_column_present(base_df=base_df, current_df=train__df, report_key_name="missing_columns_within_train_dataset")

            logging.info(f"Is all required columns present in test df")
            test_df_columns_status = self.is_required_column_present(base_df=base_df, current_df=test__df, report_key_name="missing_columns_within_test_dataset")

            if train_df_columns_status:
                logging.info(f"As all column are available in train df hence detecting data drift")
                self.data_drift(base_df=base_df, current_df=train__df, report_key_name="data_drift_within_train_dataset")
            if test_df_columns_status:
                logging.info(f"As all column are available in test df hence detecting data drift")
                self.data_drift(base_df=base_df, current_df=test__df, report_key_name="data_drift_within_test_dataset")

    


            #Write report
            logging.info("Write reprt in yaml file")
            utils.Write_ymal_file(file_path=self.data_validation_config.report_file_path,
            data=self.validation_error)

            data_validation_artifact = artifact_entity.DataValidationArtifact(report_file_path=self.data_validation_config.report_file_path,)
            logging.info(f"Data validation artifact: {data_validation_artifact}")
            return data_validation_artifact




        except Exception as e:
            raise SensorException(e, sys)

