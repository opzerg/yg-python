FROM python:3.11.4-slim

ADD ../requirements.txt /app/
WORKDIR /app/
RUN pip install --no-cache-dir -r requirements.txt

ADD ../src /app/src
WORKDIR /app/src

EXPOSE 8080