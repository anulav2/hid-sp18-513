docker-build:
        docker build -t ukugan/sshkeymgmt  .

docker-start:
        docker run -p 5000:5000 ukugan/sshkeymgmt

docker-start-detach-mode:
        docker run -d -p 5000:5000 ukugan/sshkeymgmt

docker-stop:
        docker stop $$(docker ps -a -q -f status=running)

service:
        sh start.sh
