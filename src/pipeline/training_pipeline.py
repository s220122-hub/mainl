import os
import sys
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
if __name__=="__main__":
    try:
        logging.info("training started")
        ingestion=DataIngestion()
        train_path,test_path=ingestion.initiate_data_ingestion("data/loan_data.csv")
        print("train path",train_path)
        print("test path",test_path)
    except Exception as e:
        raise CustomException(e,sys)