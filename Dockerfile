# Dockerfile
FROM python:3.11-slim

# Set work directory inside container
WORKDIR /app

# Copy installation file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project
COPY . .

# Environment settings
ENV PYTHONUNBUFFERED=1

# Run FastAPI app when the container starts
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8080"]
