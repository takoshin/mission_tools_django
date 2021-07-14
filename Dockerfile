FROM python:3.9.6-slim-buster

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive

COPY Pipfile ./
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
COPY . /usr/src/app/

RUN mkdir -p tmp/sockets \
    && apt-get update \
    && apt-get install -y gcc \
    && pip install pipenv \
    && pipenv install --system --skip-lock \
    && pip uninstall -y pipenv virtualenv-clone virtualenv

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
CMD uwsgi --ini ./uwsgi/uwsgi.ini
