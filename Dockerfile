# Use the official Python image as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files to the container
COPY app.py .

# Expose port 8080 for Flask app
EXPOSE 8080

# Start the Flask application when the container starts
CMD ["python", "app.py"]
