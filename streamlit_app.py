import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from src.myfirstmlproject.pipelines.prediction_pipeline import CustomData, PredictPipeline

# Function to make predictions
def predict(data):
    custom_data = CustomData(
        gender=data['gender'],
        race_ethnicity=data['race_ethnicity'],
        parental_level_of_education=data['parental_level_of_education'],
        lunch=data['lunch'],
        test_preparation_course=data['test_preparation_course'],
        reading_score=float(data['reading_score']),
        writing_score=float(data['writing_score'])
    )
    pred_df = custom_data.get_data_as_data_frame()
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)
    return results[0]

# Streamlit app
st.title("Student Performance Prediction")

st.sidebar.header("Input Features")

gender = st.sidebar.selectbox('Gender', ['male', 'female'])
race_ethnicity = st.sidebar.selectbox('Race/Ethnicity', ['group A', 'group B', 'group C', 'group D', 'group E'])
parental_level_of_education = st.sidebar.selectbox('Parental Level of Education', [
    'some high school', 'high school', 'some college', 'associate\'s degree', 'bachelor\'s degree', 'master\'s degree'])
lunch = st.sidebar.selectbox('Lunch', ['standard', 'free/reduced'])
test_preparation_course = st.sidebar.selectbox('Test Preparation Course', ['none', 'completed'])
reading_score = st.sidebar.slider('Reading Score', 0, 100, 50)
writing_score = st.sidebar.slider('Writing Score', 0, 100, 50)

input_data = {
    'gender': gender,
    'race_ethnicity': race_ethnicity,
    'parental_level_of_education': parental_level_of_education,
    'lunch': lunch,
    'test_preparation_course': test_preparation_course,
    'reading_score': reading_score,
    'writing_score': writing_score
}

if st.button('Predict'):
    result = predict(input_data)
    st.success(f'The predicted math score is: {result}')
