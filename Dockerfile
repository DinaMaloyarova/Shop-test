FROM python:3.8.3-slim-buster
ENV PYTHONUNBUFFERED = 1
WORKDIR src
COPY requirements.txt .
COPY src/ .
RUN pip install -r requirements.txt

