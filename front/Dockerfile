FROM python:3.7-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /src
WORKDIR /src
ADD ./front /src/

RUN pip install -r requirements.txt

EXPOSE 8000