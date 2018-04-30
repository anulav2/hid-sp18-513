FROM python:2.7

MAINTAINER Uma Kugan <ukugan@iu.edu>

RUN apt-get update
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /sshkeymgmt
WORKDIR /sshkeymgmt
RUN pip install -r requirements.txt

EXPOSE 5001
EXPOSE 5002
EXPOSE 5003
EXPOSE 5004
EXPOSE 5005

ENTRYPOINT ["make", "service"]
