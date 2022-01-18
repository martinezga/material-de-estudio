FROM python:3.9.5-slim-buster

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

WORKDIR /opt/app

ADD requirements.txt /opt/app/

RUN apt-get -q -y update \
    && apt-get -q -y install nano \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

ADD /app /opt/app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /opt/app

# USER appuser

CMD gunicorn app.wsgi --bind 0.0.0.0:$PORT
