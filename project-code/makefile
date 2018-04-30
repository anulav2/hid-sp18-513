docker-build:
        docker build -t ukugan/sshkeymgmt  .

docker-start:
        docker run -p 5000:5000 ukugan/sshkeymgmt

docker-start-detach-mode:
        docker run -d -p 5000:5000 ukugan/sshkeymgmt

docker-stop:
        docker stop $$(docker ps -a -q -f status=running)

service:
        python request_access.py
        python request_validation.py
        python create_ssh_key.py
        python sshkeycopy.py
        python getstatus.py
