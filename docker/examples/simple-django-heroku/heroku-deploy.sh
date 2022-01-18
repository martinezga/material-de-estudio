#!/bin/sh

heroku container:login
docker build -t registry.heroku.com/simple-django-docker/web .
docker push registry.heroku.com/simple-django-docker/web
heroku container:release web -a simple-django-docker
# First time deploy:
# heroku ps:scale web=1 -a simple-django-docker
heroku logs --tail -a simple-django-docker
