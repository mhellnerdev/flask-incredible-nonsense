# pull container from docker hub
FROM python:3-alpine

# set docker OS level env variables
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=run.py

# apt install required OS dependencies that allow gcc to compile the python package requirements correctly
RUN apk update && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev

# using ufw to open port 80 http
RUN apk add ufw
RUN ufw allow http

# create folder on container os for flask app to live
RUN mkdir /incrediblenonsense

# define working dir for docker to use for copy processes
WORKDIR /incrediblenonsense

# copy python package dependency file
COPY requirements.txt /incrediblenonsense

# use pip to install packages on container os that are defined in the requirements.txt
RUN pip install -r requirements.txt

# copy contents of . or local hosts folder to the WORKDIR on the container
COPY . /incrediblenonsense/

# next line has been commented out, use this command to run in development mode
CMD flask --app app.py --debug run --host=0.0.0.0 --port=5000

# run bash script to start PRODUCTION Flask server via UWSGI/gunicorn production engine
# CMD ./gunicorn.sh


'''
#### NOTES ####
# This file is currently !setup to run the bash script ./gunicorn.sh. This 
launches the flask server with multi thread workers to handle requests. 
Without this you cannot have concurrent http requests.


- docker command to run container mapping to http port and passing environment variable for debug mode true.
- this is to be used only when running in development mode
- docker run -p 80:<port defined in app.run> -e DEBUG=1 <image name>

'''