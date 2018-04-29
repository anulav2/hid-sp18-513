docker-build:
	docker build -t ukugan/flask .
	
docker-start:
	docker run -p 8080:8080 ukugan/flask
	
docker-start-detach-mode:
	docker run -d -p 8080:8080 ukugan/flask

docker-stop:
	docker stop $$(docker ps -a -q -f status=running)

service:
	sudo python request_access.py
	sudo python request_validation.py
	sudo python create_ssh_key.py
	sudo python sshkeycopy.py
	sudo python getstatus.py
