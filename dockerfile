# We're using the official Python image as the base image.
FROM python:3.8

# Working directory in our container
WORKDIR /app

# Copy requirements file into container and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -q --no-cache-dir -r requirements.txt

# Copy remaining application code into container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Default command
CMD ["python", "app.py"]
