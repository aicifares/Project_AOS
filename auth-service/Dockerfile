# Start from official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (so Docker caches this layer)
COPY requirements.txt .

# Install all dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project code
COPY . .

# Expose the port Django will run on
EXPOSE 8081

# Command to start the server when the container runs
CMD ["python", "manage.py", "runserver", "0.0.0.0:8081"]