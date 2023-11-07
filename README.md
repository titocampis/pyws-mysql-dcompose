# Python Web Server (Flask) created using Docker and configured using Ansible

## 1. App configuration

## 2. Building the services
### 2.1 Building Web Server
The web server image configuration is in [Dockerfile](Dockerfile).

Pull the `ubuntu:20.04` image:
```bash
docker pull ubuntu:20.04
```

Build the configured image with the needed to run the webserver using the custom Dockerfile:
```bash
docker build -t python_webserver .
```

### 2.2 Building and configuring Mysql
We are going to use the base image of mysql [mysql:5.7](https://hub.docker.com/_/mysql), so no Dockerfile is needed.

The configuration of the mysql is in [docker-compose.yaml](docker-compose.yaml):

| **Configuration** |  |
| :---: | :---: |
| **MYSQL_DATABASE** | db |
| **MYSQL_USER** | user |
| **MYSQL_PASSWORD** | password |
| **MYSQL_ROOT_PASSWORD** | password |

## 2. Running the services