#
# Football-API Dockerfile
#
#


#Pull base image.

FROM python:3.4.5-slim

#Get some packages
#RUN apt-get update && apt-get install -y \
#    build-essential \
#    make \
#    gcc \
#    python3-dev \
#    mongodb \

#Local directory
#RUN mkdir /opt/football-api

#set "football-api" as the working directory
WORKDIR /app

#copy files
#ADD . .
COPY ./requirements.txt .

#pip install requirements.txt
RUN pip install -r requirements.txt
RUN pip install requests

#Listen to port 5000
EXPOSE 5000

#Start the app server
CMD python app.py