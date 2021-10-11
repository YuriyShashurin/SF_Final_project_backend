# syntax=docker/dockerfile:1
FROM python
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/