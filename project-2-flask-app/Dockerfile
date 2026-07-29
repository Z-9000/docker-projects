FROM python:3.12-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

# Copy ONLY requirements.txt first, install deps, THEN copy the rest of the code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

EXPOSE 5000

CMD ["python", "app.py"]