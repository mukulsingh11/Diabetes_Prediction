import os,sys
import numpy as np
import pandas as pd
from diabetes.logger import logging
from diabetes.exception import CustomException
from dataclasses import dataclass
from sklearn.model_selection import train_test_split


@dataclass

class DataIngestionConfig:
    train_data_path : str = os.path.join('artifacts' , 'train.csv')
    test_data_path : str = os.path.join('artifacts' , 'test.csv')
    raw_data_path : str = os.path.join('artifacts' , 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def inititate_data_ingestion(self):
        logging.info(f"********************   Data Ingestion is Started   ***********************")
        try:

            df = pd.read_csv('diabetes_prediction_dataset (1).csv')
            logging.info(f"read the dataset")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info(f'Trian_Test_Split')
            train_set ,test_set = train_test_split(df , test_size=0.30 , random_state=30)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False , header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False , header=True)

            logging.info(f"********** Data Ingestion is Conpleted *************")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj = DataIngestion()
    train_data ,test_data = obj.inititate_data_ingestion()


