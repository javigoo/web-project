FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /django
WORKDIR /django

RUN useradd -ms /bin/bash user
USER user

COPY requirements.txt /django/
RUN pip install -r requirements.txt
