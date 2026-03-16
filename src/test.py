from src.logger import logging
from src.exception import CustomException
import sys
if __name__=="__main__":
    try:
        logging.info("logging started")
        a=1/0
    except Exception as e:
        raise CustomException(e,sys)