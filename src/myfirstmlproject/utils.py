import os
import sys
from src.myfirstmlproject.exception import CustomException
from src.myfirstmlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
import pymysql

import pickle
import numpy as np

load_dotenv()

host=os.getenv("mysql_host")
user=os.getenv("mysql_user")
password=os.getenv("mysql_password")
db=os.getenv('mysql_database')


# Print retrieved environment variables for debugging
print("Host:", host)
print("User:", user)
print("Password:", password)
print("Database:", db)

# Check if any environment variables are None
if None in [host, user, password, db]:
    raise ValueError("One or more environment variables are not set.")





def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established: %s", mydb)

        
        df=pd.read_sql_query('Select * from students',mydb)
        print(df.head())

        return df



    except Exception as ex:
            error_message = "An unexpected error occurred during data ingestion"
            error_details = str(ex)  # Include the original exception message for additional context
            logging.exception("Custom Exception occurred: %s", error_details)  # Log the original exception traceback
            raise CustomException(error_message, error_details)

    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as ex:
            error_message = "An unexpected error occurred during data ingestion"
            error_details = str(ex)  # Include the original exception message for additional context
            logging.exception("Custom Exception occurred: %s", error_details)  # Log the original exception traceback
            raise CustomException(error_message, error_details)


def evaluate_models(X_train, y_train,X_test,y_test,models,param):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as ex:
            error_message = "An unexpected error occurred during data ingestion"
            error_details = str(ex)  # Include the original exception message for additional context
            logging.exception("Custom Exception occurred: %s", error_details)  # Log the original exception traceback
            raise CustomException(error_message, error_details)
    


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as ex:
            error_message = "An unexpected error occurred during data ingestion"
            error_details = str(ex)  # Include the original exception message for additional context
            logging.exception("Custom Exception occurred: %s", error_details)  # Log the original exception traceback
            raise CustomException(error_message, error_details)

