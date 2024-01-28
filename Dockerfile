FROM python:3.9-alpine3.16

COPY requirements.txt /temp/requirements.txt
COPY recipe_app /recipe_app

WORKDIR /recipe_app

EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev
RUN pip install --no-cache-dir -r /temp/requirements.txt
RUN adduser --disabled-password service-user

USER service-user