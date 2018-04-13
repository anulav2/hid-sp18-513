SWAGGERCODEGEN=java -jar swagger-codegen-cli-2.3.1.jar
YAML=string_init.yaml
DATA=data
DESTDIR=server/
FLASKDIR=server/string/flaskConnexion

dest:
	mkdir $(DESTDIR)

service: 
	sudo wget https://oss.sonatype.org/content/repositories/releases/io/swagger/swagger-codegen-cli/2.3.1/swagger-codegen-cli-2.3.1.jar
	$(SWAGGERCODEGEN) generate  -i $(YAML)  -l python-flask  -o $(FLASKDIR)  -D supportPython2=true
	mkdir $(DATA)
	touch $(DATA)/data.csv
	cp -r data $(FLASKDIR)
	cp -r default_controller.py $(FLASKDIR)/swagger_server/controllers

run: 
	cd $(FLASKDIR) && pip install -r requirements.txt && \
	sudo python setup.py install && python -m swagger_server

test:
	curl http://localhost:8080/cloudmesh/addString/adding-a-new-string
	curl http://localhost:8080/cloudmesh/fetchString/3
	            
stop:
	ps -ef | grep swagger | grep -v "grep"| awk '{print $$2}' | xargs kill -9

clean:
	sudo rm -r $(DESTDIR)

container:
	sudo docker build -t cloudmesh-strings .
	sudo docker run -p 8080:8080 cloudmesh-strings 

osx:
	docker build -t cloudmesh-strings .
	docker run -p 8080:8080 cloudmesh-strings 
