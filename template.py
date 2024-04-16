import os
import os.path
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = 'myfirstmlproject'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_trasnformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"  # Added missing comma here
]

for filepath in list_of_files:
    filepath_obj = Path(filepath)  # Renamed variable to filepath_obj
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    full_filepath = os.path.join(filedir, filename)  # Creating full file path here

    if (not os.path.exists(full_filepath)) or (os.path.getsize(full_filepath) == 0):
        with open(full_filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {full_filepath}")

    else:
        logging.info(f"{filename} is already existing")
