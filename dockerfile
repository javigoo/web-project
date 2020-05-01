FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /django
WORKDIR /django

COPY requirements.txt /django/
RUN pip install -r requirements.txt
