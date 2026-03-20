# Use the official Python image from the Docker Hub
FROM python:3.13-slim

# Prevent python from writing pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Enable real-time logging
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /code

# Copy the requirements file first to leverage Docker cache for dependencies
COPY ./requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application code and other necessary files
COPY ./app /code/app
COPY ./models /code/models
COPY ./generate_training_data.py /code/generate_training_data.py
COPY ./train_model.py /code/train_model.py
COPY ./training_data.csv /code/training_data.csv

# Expose internal port
EXPOSE 8000

# Start Gunicorn with Uvicorn workers
CMD ["gunicorn", "app.main:app", "-k", "uvicorn.workers.UvicornWorker", "-w", "2", "-b", "0.0.0.0:8000", "--forwarded-allow-ips", "*", "--access-logfile", "-", "--error-logfile", "-"]