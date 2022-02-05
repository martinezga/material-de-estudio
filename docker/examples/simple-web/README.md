# Simple web

Project created to teach how deploy a simple web application using Docker and Nginx as server to girls of Skill for Women in Tech - México 2022.

## App deploy using Docker:

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
