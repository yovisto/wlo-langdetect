FROM python:buster

RUN pip3 install --upgrade pip
RUN pip3 install cherrypy
RUN pip3 install langdetect

