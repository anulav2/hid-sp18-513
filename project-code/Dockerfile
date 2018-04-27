FROM python:2.7

MAINTAINER Uma Kugan <ukugan@iu.edu>

ARG GIT_COMMIT=unspecified
LABEL git_commit=$GIT_COMMIT

RUN apt-get update
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "/app/app/main.py"]
