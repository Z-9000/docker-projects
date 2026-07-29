# 1. Start from an official base image that already has Python installed
FROM python:3.12-slim

# 2. Set the working directory inside the container
WORKDIR /app

# Force Python to flush output immediately instead of buffering it
ENV PYTHONUNBUFFERED=1

# 3. Copy our script into the container's working directory
COPY app.py .

# 4. Define the command that runs when the container starts
CMD ["python", "app.py"]