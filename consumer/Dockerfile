FROM python:3.10-slim

RUN apt-get update && apt-get install -y nano

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "run_consumer.py"]