# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the local code to the container image
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Command to run the Lambda function
CMD ["python", "lambda_function.py"]
