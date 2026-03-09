# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Set environment variables
# PORT is set to 7234 as per README requirements
ENV PORT=7234
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data required by the chatbot engine
RUN python -m nltk.downloader punkt wordnet omw-1.4

# Copy the rest of the application code
COPY . .

# Ensure the project structure matches Flask's expectations
# Move index.html to templates folder if it exists in the root
RUN mkdir -p templates static && \
    if [ -f index.html ]; then mv index.html templates/; fi

# Expose the port the app runs on
EXPOSE 7234

# Use gunicorn for a production-ready deployment
# We bind to the PORT environment variable
CMD gunicorn --bind 0.0.0.0:$PORT app:app
