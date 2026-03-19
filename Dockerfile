# Use the official Python 3.13 slim image for maximum async performance and security
FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Install system dependencies (specifically FFmpeg for the Static Fallback Mode)
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY infrastructure/requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY infrastructure/app.py .
COPY backend/ ./backend/

# Expose the port the Cloud Run app runs on
EXPOSE 8080

# Run the Flask orchestration application
CMD ["python", "app.py"]