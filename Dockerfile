# Installing ubuntu:20.04 image
FROM ubuntu:20.04

# Updating and upgrading the system
RUN apt-get update && apt-get upgrade -y

# Installing python libraries
RUN apt-get install -y python3 python3-pip

# Install python modules
RUN pip install flask mysql-connector-python

# Copy the web application python file into /opt directory
COPY app.py /opt/

# Run the webservice once the container starts
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080