FROM python:2.7

MAINTAINER Uma M Kugan <ukugan@iu.edu>

# Setup java 
RUN apt-get update
RUN apt-get install -q -y default-jre

# install net tools
RUN apt-get install -q -y net-tools

COPY ["Makefile", "cpu.yaml", \
      "default_controller.py",\
      "requirements.txt", "swagger-codegen-cli.jar", "/files/"]

WORKDIR /files
  
RUN pip install -r requirements.txt

# tell the port number the container should expose
EXPOSE 8080

# Install the flask service using make commands
RUN make service

# start the service
CMD ["make", "start"]
