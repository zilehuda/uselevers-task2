FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /app2

COPY ./requirements.txt /app2/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app2/requirements.txt

COPY . /app2/