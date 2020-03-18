FROM python:3.7

ENV PYTHONUNBUFFERED=1

RUN mkdir /src

COPY requirements.txt /src
RUN pip install -r src/requirements.txt

COPY . /src