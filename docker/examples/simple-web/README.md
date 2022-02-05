# Simple web

Project created to teach how deploy a simple web application using Docker and Nginx as server to girls of Skill for Women in Tech - México 2022.

### Image available at:

https://hub.docker.com/r/martinezga/simple-web

## How run the app using the image from Docker hub:


## How deploy using the Dockerfile:

Crear la imagen:

        $ docker build -t image_name .

Verificar que la imagen está creada:

        $ docker image ls

Crear un contenedor:

        $ docker run -d --rm -p 80:80 --name container_name image_name

Detener el contenedor:

        $ docker stop container_name

Entrar al contenedor / Inspeccionar el contenido del contenedor:

        $ docker exec -it container_name sh

Crear un contenedor que incluya un "bind volume" para ver los cambios reflejados en tiempo real:

        $ docker run -d --rm -p 80:80 --name container_name --mount type=bind,source="$(pwd)"/web,target=/usr/share/nginx/html/ image_name

### Technologies used:

- Docker
- Nginx
- Vanilla HTML, CSS, JS
- https://some-random-api.ml/endpoints


### How tag and deploy an image to Docker Hub:

        $ docker login
        $ docker tag simple-web:latest martinezga/simple-web:latest
        $ docker push martinezga/simple-web:latest

### Do you want to create your own project?

Visit this tutorial:

https://www.docker.com/blog/how-to-use-the-official-nginx-docker-image/
