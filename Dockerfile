# Installing ubuntu:20.04 image
FROM ubuntu:20.04

# Updating, upgrading the system and installing python libraries
RUN apt-get update && apt-get install -y python3 python3-pip

# Install flask python framework
RUN pip install flask 

# Copy the web application python file into /opt directory
COPY app.py /opt/

# Run the webservice once the container starts
ENTRYPOINT FLASK_APP=/opt/app.py flask run --host=0.0.0.0 --port=8080