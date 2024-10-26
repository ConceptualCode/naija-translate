# Use the official Python 3.10 base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app code to the container
COPY . .

# Expose port 7860 (expected by Hugging Face Spaces)
EXPOSE 7860

# Run the FastAPI app with Uvicorn
CMD ["uvicorn", "apis:app", "--host", "0.0.0.0", "--port", "7860"]
