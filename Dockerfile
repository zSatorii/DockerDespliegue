FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install --no-cache-dir --upgrade pip setuptools msgpack

COPY . .

EXPOSE 5050
CMD ["python3", "sample_app.py"]