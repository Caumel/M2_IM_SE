FROM python:3.7-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /src
WORKDIR /src
ADD ./web /src/

RUN pip install -r requirements.txt