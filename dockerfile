# We're using the official Python image as the base image.
FROM python:3.8

# Working directory in our container
WORKDIR /app

# Copy requirements file into container and install dependencies
COPY requirements1.txt .
COPY requirements2.txt .
RUN pip install --upgrade pip
RUN python -m venv venv
RUN . venv/bin/activate
RUN pip install --no-cache-dir -r requirements1.txt
RUN pip install --no-cache-dir -r requirements2.txt

# Copy remaining application code into container
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Default command
CMD ["python", "app.py"]
