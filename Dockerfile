FROM python:3.8.6-alpine

LABEL project="short_urls"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system --ignore-pipfile

COPY short_urls /code/


