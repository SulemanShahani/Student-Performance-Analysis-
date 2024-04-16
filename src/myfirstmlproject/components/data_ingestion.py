import os

from src.myfirstmlproject.exception import CustomException
from src.myfirstmlproject.logger import logging
import pandas as pd



from sklearn.model_selection import train_test_split

from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
     
     
            
            
            
            df=pd.read_csv(os.path.join('notebook/data','raw.csv'))
            logging.info("Reading database is completed")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("splitting data into train and test set is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path


            )


        except Exception as ex:
            error_message = "An unexpected error occurred during data ingestion"
            error_details = str(ex)  # Include the original exception message for additional context
            logging.exception("Custom Exception occurred: %s", error_details)  # Log the original exception traceback
            raise CustomException(error_message, error_details)
