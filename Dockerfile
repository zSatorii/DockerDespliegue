FROM python:3.12-slim

WORKDIR /app

RUN pip install --upgrade pip setuptools

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install --upgrade msgpack

COPY . .

EXPOSE 5050
CMD ["python3", "sample_app.py"]