# Siguiendo el tutorial de Docker Desktop
https://www.docker.com/101-tutorial

1. Open Docker Desktop
2. Type the following command in your terminal: 

    ```docker run -dp 80:80 docker/getting-started```

3. Open your browser to http://localhost
4. Have fun!

## Alternativa sin instalar nada: Play with Docker
https://labs.play-with-docker.com/

Type the following command in your PWD terminal: 

```docker run -dp 80:80 docker/getting-started:pwd```

08/05/2021

### Container Networking

Remember this rule...

> If two containers are on the same network, they can talk to each other. If they aren't, they can't.

There are two ways to put a container on a network: 1) Assign it at start or 2) connect an existing container.

Create the network. ```docker network create todo-app```

To confirm we have the database up and running, connect to the database and verify it connects.

```docker exec -it <mysql-container-id> mysql -p```


docker run algo crea, ejecuta y se detiene el contenedor
docker container ls muestra solo los containers que se están ejecutando en ese momento
docker container ls -a muestra todos los contenedores estén activos o detenidos
docker container run --name hola hello-world ejecuta y crea el contenedor con el nombre indicado
docker container start hola (nombre del contenedor o ID) para iniciar un contenedor previamente creado lo ejecuta en el background
docker container run --name ubuntutest -it ubuntu /bin/bash para 
docker container exec -it -u root hola /bin/bash ejecutar el contenedor de forma interactiva y que no se detenga
docker attach ubuntutest se ejecuta y vuelve a conectar en la terminal

crear una imagen base con debian y python
En hub docker busco la imagen oficial de debian 

docker images -a lista todas las imagenes. Tenemos varios contenedores basados en 2 imagenes
Es mejor usar etiquetas en las imágenes para tener mayor control de las versiones que se están usando

docker pull debian:9.11 con la imagen creada puedo crear un contenedor docker container run --name debiantest -it debian:9.11 /bin/bash

apt install top > apt top > htop
docker container exec -it -u root debiantest echo "hola"
para conectarse al contenedor principal docker container exec -it -u root debiantest /bin/bash

```a```
```a```
```a```
```a```
```a```
```a```