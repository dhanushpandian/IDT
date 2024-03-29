# Use the official Python image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir Flask\
    Flask-Cors \
    pandas\
    scikit-learn \
    matplotlib\
    numpy

# Expose the port that the Flask app runs on
EXPOSE 5000

# Command to run the Flask app when the container starts
CMD ["python", "app.py"]
