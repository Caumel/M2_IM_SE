FROM python:3.7-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /src
WORKDIR /src
ADD ./front /src/

RUN pip install pipenv
RUN pipenv install --system

EXPOSE 8000