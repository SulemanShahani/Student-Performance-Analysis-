# Importing necessary modules
import logging
import sys
from src.myfirstmlproject.components.data_ingestion import DataIngestion, DataIngestionConfig

from src.myfirstmlproject.components.data_transformation import DataTransformationConfig, DataTransformation

from src.myfirstmlproject.components.model_trainer import ModelTrainer, ModelTrainerConfig 

from src.myfirstmlproject.exception import CustomException

def initiate_data_ingestion():
    """
    Function to initiate the data ingestion process.
    """
    try:
        logging.info("Starting the data ingestion process.")
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion process completed successfully.")

        
    
    except CustomException as e:
        logging.error(f"Custom Exception occurred: {e}")
        raise
    
def initiate_data_transformation():
    """
    Function to initiate the data transformation process.
    """
    try:
        logging.info("Starting the data transformation process.")
        train_path = r"artifacts\train.csv"
        test_path = r"artifacts\test.csv"
        data_transformation = DataTransformation()
        train_array,test_array,_= data_transformation.initiate_data_transformation(train_path,test_path)
        logging.info("Data transformation process completed successfully.")
        return train_array, test_array

    except CustomException as e:
        logging.error(f"Custom Exception occurred: {e}")
        raise
    


def initiate_model_training(train_array, test_array):
    """
    Function to initiate the model training process.
    """
    try:
        logging.info("Starting the model training process.")
        
        model_trainer = ModelTrainer()

        
        model_trainer.initiate_model_trainer(train_array,
                test_array)

        logging.info("Model training process completed successfully.")

    except CustomException as e:
        logging.error(f"Custom Exception occurred: {e}")
        raise  


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:


        initiate_data_ingestion()
        train_array, test_array=initiate_data_transformation()
       
        
        initiate_model_training(train_array,test_array)
    except CustomException as ce:
        logging.error(f"Custom Exception occurred during data ingestion: {ce}")
   
