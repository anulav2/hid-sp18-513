## FLASK API to copy the ssh public key from one server to another server 
  
* Three API endpoints are provided.

  * ```/request_access```
  
  * ```/validate_and_action```
  
  * ```/create_ssh_key```
  
  * ```/copy_ssh_key```  
 
   * ```/getstatus```
   
## Instructions for docker installation

* git clone the project.

* you should install docker.


* Build the image from docker file

	* ``` make docker-build ```

* Start the service using following make command
  
  * ```make docker-start```

* Test the service using following curl commands or run sh curlall.sh
  
  
  * ```curl -H "Content-Type: application/json" -X POST -d '{"src_host":"gani-VirtualBox", "src_user":"gani", "src_key":"/home/gani/.ssh/id_rsa.pub", "tgt_host":"gani-VirtualBox", "tgt_user":"nemo","req_by":"Uma"}' http://localhost:5000/request_access```
  
  * ```curl -H "Content-Type: application/json" -X POST -d '' http://localhost:5000/validate_and_action```     
  
  * ```curl -H "Content-Type: application/json" -X POST -d '{"src_host":"gani-VirtualBox", "src_user":"gani"}' http://localhost:5000/create_ssh_key```

  * ```curl -H "Content-Type: application/json" -X POST -d '{"src_host":"gani-VirtualBox", "src_user":"gani", "src_pub_key":"/home/gani/.ssh/id_rsa.pub", "tgt_host":"gani-VirtualBox", "tgt_user":"nemo","req_processed_by":"gani"}' http://localhost:5000/copy_ssh_key```

  * ```curl -H "Content-Type: application/json" -X POST -d '' http://localhost:5000/getstatus/APPROVED```
  
   * ```curl -H "Content-Type: application/json" -X POST -d '' http://localhost:5000/getstatus/DECLINED```
  
* Get the container ID using following command
  
  * ```docker ps```

* Stop the service using following commands
  
  * ```make docker-stop```

* Optional starting mechanism (interactive mode)
  
  * ```make start``` 
  
  * ```make stop```
	
## Instructions for ubuntu without docker

* you should be running this program in python 2 environment.

* you should have default-jre installed.

* git clone the project.


* Ensure Python 2 environment is activated

	* ``` pyenv activate env2 (Refer handbook for details ```
	
VIDEO DEMONSTARTION: 

A video demonstartion of the project is provided [video]https://youtu.be/LPQS-PZpiD4.
  
  



