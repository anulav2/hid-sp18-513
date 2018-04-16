SWAGGER_CODEGEN=java -jar swagger-codegen-cli.jar
YML=sysinfo.yaml
HOME=server
CLIENT=client
CONFIG=$(HOME)/config
DATA=$(HOME)/data
CONTR=$(HOME)/swagger_server/controllers


docker-build:
	docker build -t uma/swagger .

docker-start:
	docker run -p 8080:8080 uma/swagger
	
docker-stop:
	docker stop $$(docker ps -a -q -f status=running)

service:
	#creates the swagger service from the yaml file and places the controllers in the appropriate directory
	$(SWAGGER_CODEGEN) generate -i $(YML) -l python-flask -o $(HOME) -D supportPython2=true
	cp *_controller.py $(CONTR)
	cp requirements.txt $(HOME)
	# Install dependencies and server side code
	cd $(HOME); pip install --upgrade pip; pip install -r requirements.txt; python setup.py install; cd ..;
	
	
start:
	#starts the services
	cd $(HOME); python -m swagger_server; cd ..;

stop:
	#stops the service
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9


test-cpu:
	echo "Testing get cpu info API"
	curl -H "Content-Type:application/json" -X GET http://localhost:8080/api/cpu

test-disk:
	echo "Testing get disk info API"
	curl  -H "Content-Type:application/json" -X GET http://localhost:8080/api/disk

test-ram:
	echo "Testing get ram info API"
	curl  -H "Content-Type:application/json" -X GET http://localhost:8080/api/ram
	
clean: 
	# removes the code generated
	if [ -d $(HOME) ]; then rm -r $(HOME); fi
	

