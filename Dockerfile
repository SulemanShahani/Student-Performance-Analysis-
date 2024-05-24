FROM python:-slim-buster

WORKDIR /app

COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8080

# Command to run the application
CMD ["python", "application.py"]
