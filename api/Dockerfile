FROM python:3.8.0-buster

WORKDIR /usr/src/api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 

RUN apt update

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/api/requirements.txt
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/api/entrypoint.sh

COPY . /usr/src/api/

ENTRYPOINT ["/usr/src/api/entrypoint.sh"]

