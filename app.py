# Importing necessary modules
import logging
import sys
from src.myfirstmlproject.components.data_ingestion import DataIngestion, DataIngestionConfig
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
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        initiate_data_ingestion()
    except CustomException as ce:
        logging.error(f"Custom Exception occurred during data ingestion: {ce}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
