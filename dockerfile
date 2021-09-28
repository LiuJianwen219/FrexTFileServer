FROM python:3.6.14-stretch

# create workspace
WORKDIR /FrexT

# initial python environment
COPY requirements.txt /FrexT/requirements.txt
RUN ["pip", "install", "-r", "requirements.txt"]

# copy application files
COPY ./ /FrexT/FrexTFileServer/

# expose port
EXPOSE 8010/tcp

#ENTRYPOINT ["uwsgi", "--ini", "FrexTFileServer/FrexTFileServer.ini"]
