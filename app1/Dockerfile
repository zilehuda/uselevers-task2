FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app1

COPY ./requirements.txt /app1/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app1/requirements.txt

COPY . /app1/