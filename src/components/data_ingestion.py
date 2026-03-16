import os
import sys
import yaml
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exception import CustomException
class DataIngestion:
    def __init__(self,config_path="config.yaml"):
        try:
            # yaml loading
            with open(config_path) as file:
                self.config=yaml.safe_load(file)
                self.raw_data_path=self.config["data_ingestion"]["raw_data_path"]
                self.train_data_path=self.config["data_ingestion"]["train_data_path"]
                self.test_data_path=self.config["data_ingestion"]["test_data_path"]
            os.makedirs(os.path.dirname(self.raw_data_path),exist_ok=True)
        except Exception as e:
            raise CustomException(e,sys)
    def initiate_data_ingestion(self,source_path):
        try:
            logging.info("data ingestion started")
            df=pd.read_csv(source_path)
            logging.info("data is loaded successfully")
            df.to_csv(self.raw_data_path,index=False)
            logging.info("raw data is saved")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.train_data_path,index=False)
            test_set.to_csv(self.test_data_path,index=False)
            logging.info("training and testing data is saved")
            return self.train_data_path,self.test_data_path
        except Exception as e:
            raise CustomException(e,sys)
    