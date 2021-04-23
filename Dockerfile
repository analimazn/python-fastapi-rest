# pull official base image
FROM python:3.8.1-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements file
COPY ./requirements.txt /app/requirements.txt

# install dependencies
RUN pip install -r /app/requirements.txt

# copy project
COPY . /app/