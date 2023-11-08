# Python Web Server (Flask) created using Docker and configured using Ansible

## 1. Python App

### 1.1 Introduction
This web application is a simple web application to manage a `mysql` db. It is coded in python using the `Flask` framework to develop a **Web Server Controller** to manage request, perform tasks and render templates to show on the exposed port (8080)

### 1.2 app.py


## 2. Docker Compose
### 2.1 Building and configuring Mysql Service
We are going to use the base image of mysql [mysql:5.7](https://hub.docker.com/_/mysql), so no Dockerfile is needed.

The configuration of the mysql is in [docker-compose.yaml](docker-compose.yaml) and in the [.env](.env) file:

| **Configuration** |  |
| :---: | :---: |
| **MYSQL_DATABASE** | db |
| **MYSQL_USER** | user |
| **MYSQL_PASSWORD** | password |
| **MYSQL_ROOT_PASSWORD** | password |

Pull the `mysql:5.7` image:
```bash
docker pull mysql:5.7
```

The database service will be running on container port: `3306`. And it will be binded to localhost:`3306`. But it is not actually needed to bind it, because the web server is going to consume it via the `docker network`

### 2.2 Building Web Server Service
The web server image configuration is in [Dockerfile](Dockerfile).

Pull the `ubuntu:20.04` image:
```bash
docker pull ubuntu:20.04
```

Build the configured image with the needed to run the webserver using the custom Dockerfile:
```bash
docker build -t python-ws .
```

> :paperclip: **NOTE:** [.dockerignore](.dockerignore) file contains the directories / files to not to be included when copy or add in the docker image.

The web application service will be running on container port: `8080`. And it will be binded to localhost:`8080` port.

### 2.3 Running the services
User docker compose to run both services:
```bash
docker compose up -d
```

When you want to stop the services
```bash
docker compose down
```