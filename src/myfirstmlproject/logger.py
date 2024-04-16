import logging
import os
from datetime import datetime

# Create a directory to store log files
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)

# Generate log file name with current timestamp
log_file = datetime.now().strftime('%m_%d_%Y_%H_%M_%S') + ".log"

# Set up logging configuration
logging.basicConfig(
    filename=os.path.join(log_dir, log_file),
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
