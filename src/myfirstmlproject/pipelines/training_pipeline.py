import os
import pandas as pd
from src.myfirstmlproject.exception import CustomException
from src.myfirstmlproject.utils import save_object
from src.myfirstmlproject.logger import logging

class TrainPipeline:
    def __init__(self):
        pass

    def train(self, data):
        try:
            # Perform data preprocessing and feature engineering
            preprocessed_data = self.preprocess_data(data)

            # Train the model
            trained_model = self.train_model(preprocessed_data)

            # Save the trained model
            self.save_model(trained_model)

            # Optionally, return the trained model
            return trained_model
        
        except Exception as ex:
            error_message = "An unexpected error occurred during model training"
            error_details = str(ex)  # Include the original exception message for additional context
            logging.exception("Custom Exception occurred: %s", error_details)  # Log the original exception traceback
            raise CustomException(error_message, error_details)

    def preprocess_data(self, data):
        # Implement data preprocessing and feature engineering here
        # This could include tasks such as handling missing values, encoding categorical variables, scaling features, etc.
        preprocessed_data = data  # Placeholder for actual preprocessing logic
        return preprocessed_data

    def train_model(self, preprocessed_data):
        # Implement model training logic here
        # This could involve selecting a machine learning algorithm, training the model on the preprocessed data, tuning hyperparameters, etc.
        trained_model = None  # Placeholder for actual model training logic
        return trained_model

    def save_model(self, trained_model):
        # Specify the path to save the trained model
        model_path = os.path.join("artifacts", "trained_model.pkl")

        # Save the trained model
        save_object(trained_model, model_path)
