# Student Performance Prediction App

This is a Streamlit application that predicts student performance based on various input features. The application uses a machine learning model to predict the math score of a student.

## Features

- Predict student math scores based on:
  - Gender
  - Race/Ethnicity
  - Parental Level of Education
  - Lunch
  - Test Preparation Course
  - Reading Score
  - Writing Score

## Requirements

- Python 3.7 or higher
- Streamlit
- pandas
- scikit-learn
- Your custom prediction pipeline (`CustomData` and `PredictPipeline`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/student-performance-prediction.git
    cd student-performance-prediction
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure the following directory structure for your custom modules:
    ```
    student-performance-prediction/
    ├── src/
    │   └── myfirstmlproject/
    │       └── pipelines/
    │           ├── __init__.py
    │           ├── prediction_pipeline.py
    ├── app.py
    ├── requirements.txt
    └── README.md
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

2. Open your web browser and go to `http://localhost:8501`.

3. Input the required features in the sidebar and click "Predict" to get the predicted math score.

## File Structure

- `app.py`: The main application script.
- `requirements.txt`: A file listing the required Python packages.
- `README.md`: This file.

## Custom Prediction Pipeline

Ensure that your custom prediction pipeline is correctly implemented and located in the `src/myfirstmlproject/pipelines/prediction_pipeline.py` file. The pipeline should include:
- `CustomData`: A class for handling input data.
- `PredictPipeline`: A class for making predictions.

## Example

```python
# src/myfirstmlproject/pipelines/prediction_pipeline.py

class CustomData:
    def __init__(self, gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course, reading_score, writing_score):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        return pd.DataFrame({
            "gender": [self.gender],
            "race_ethnicity": [self.race_ethnicity],
            "parental_level_of_education": [self.parental_level_of_education],
            "lunch": [self.lunch],
            "test_preparation_course": [self.test_preparation_course],
            "reading_score": [self.reading_score],
            "writing_score": [self.writing_score]
        })

class PredictPipeline:
    def __init__(self):
        # Load your trained model here
        pass

    def predict(self, df):
        # Predict using your model
        return [70]  # Replace with actual prediction logic
