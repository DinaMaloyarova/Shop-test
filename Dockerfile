FROM python:3.8.3-slim-buster
ENV PYTHONUNBUFFERED = 1
WORKDIR src
COPY src/ .
COPY requirements.txt .
RUN pip install -r requirements.txt

