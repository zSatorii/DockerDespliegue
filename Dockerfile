FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --only-upgrade libssl3t64 openssl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir --upgrade pip setuptools msgpack

COPY . .

EXPOSE 5050
CMD ["python3", "sample_app.py"]