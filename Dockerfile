# Installing ubuntu:20.04 image
FROM ubuntu:20.04

# Updating and upgrading the system
RUN apt-get update && apt-get upgrade -y

# Installing python libraries
RUN apt-get install -y python3 python3-pip

# Install python modules - https://stackoverflow.com/questions/25981703/pip-install-fails-with-connection-error-ssl-certificate-verify-failed-certi
RUN pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org flask mysql-connector-python

# Copy the web application python files into /opt directory
COPY . /opt/

# Run the webservice once the container starts, it will use the envs for the .env file as it is run using docker compose
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=${PYTHON_HOST} --port=${PYTHON_PORT}