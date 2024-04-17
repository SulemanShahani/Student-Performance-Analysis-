import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.myfirstmlproject.utils import save_object

from src.myfirstmlproject.exception import CustomException
from src.myfirstmlproject.logger import logging
import os



@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class DataTransformation:
    
     def inspect_data(self, df):
        """
        Inspects data for missing values and unexpected string values
        """
        for col in df.columns:
            if df[col].dtype == 'object':
                if df[col].isnull().sum() > 0:
                    logging.warning(f"Column '{col}' has missing values")
                if len(df[col].unique()) > 10:
                    logging.warning(
                        f"Column '{col}' has more than 10 unique values, consider inspecting it")
            else:
                if df[col].isnull().sum() > 0:
                    logging.warning(f"Column '{col}' has missing values")


                    
    
    
    
     def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

     def get_data_transformer_object(self):
        '''
        this function is responsible for data transformation
        '''
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            num_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy='median')),
                ('scalar',StandardScaler())

            ])
            cat_pipeline=Pipeline(steps=[
            ("imputer",SimpleImputer(strategy="most_frequent")),
            ("one_hot_encoder",OneHotEncoder())
            ])

            logging.info(f"Categorical Columns:{categorical_columns}")
            logging.info(f"Numerical Columns:{numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_columns),
                    ("cat_pipeline",cat_pipeline,categorical_columns)
                ]

            )
            return preprocessor
            

        except Exception as ex:
            error_message = "An unexpected error occurred during data ingestion"
            error_details = str(ex)  # Include the original exception message for additional context
            logging.exception("Custom Exception occurred: %s", error_details)  # Log the original exception traceback
            raise CustomException(error_message, error_details)

        
     def initiate_data_transformation(self, train_path, test_path):
        try:
            logging.info("Starting the data transformation process.")
            data_transformation = DataTransformation()
            train_path = r"artifacts\train.csv" 
            test_path = r"artifacts\test.csv"

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Reading the train and test file")

            preprocessing_obj = self.get_data_transformer_object()
            target_column_name = "math_score"
            # Inspect transformed data
            logging.info("Inspecting transformed data:")
            transformed_data_train = preprocessing_obj.fit_transform(train_df.drop(columns=[target_column_name], axis=1))
            transformed_data_test = preprocessing_obj.transform(test_df.drop(columns=[target_column_name], axis=1))
            logging.info("Transformed data shape (train): %s", transformed_data_train.shape)
            logging.info("Transformed data shape (test): %s", transformed_data_test.shape)

            

            logging.info("Applying Preprocessing on training and test dataframe")

            # Divide the train dataset to independent and dependent feature
            input_features_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            # Divide the test dataset to independent and dependent feature
            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying Preprocessing on training and test dataframe")

            input_feature_train_arr = transformed_data_train
            input_feature_test_arr = transformed_data_test
            target_feature_train_arr = target_feature_train_df.values
            target_feature_test_arr = target_feature_test_df.values

            train_arr = np.c_[input_feature_train_arr, target_feature_train_arr]
            test_arr = np.c_[input_feature_test_arr, target_feature_test_arr]

            logging.info(f"Saved preprocessing object")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except Exception as ex:
            error_message = "An unexpected error occurred during data ingestion"
            error_details = str(ex)  # Include the original exception message for additional context
            logging.exception("Custom Exception occurred: %s", error_details)  # Log the original exception traceback
            raise CustomException(error_message, error_details)