## Swagger Rest API Assignment
This swagger API exploits CSV storage [/data/data.csv] to store and retrieve string data.
 
 ### Specification:
 * String_init.yaml
 
 ### Setup:
 * gitclone the codebase
 * MakeFile provided will generate the required code using the following command:
    * `make service`
    This is install the necessary folder origanization needed for swagger rest API
    * `make run`
    This will run the Flask server at localhost:8080. To make sure the setup is up and running you should see the following massage in       the console:
    ``` 
     Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
    ```
    * Now you can test the API either by system bowser or using the following command in a separate console window:
        `make test`
    * Once done testing the server can be stopped using cntrl+c on the console showing the server logs or by running the following the         separate broswer console: 
       `make stop`
    * finally the following command will clean the created folder structure for the API testing:
       `make clean`
    * for the docker image:
      `make container`
    * To run the service:
    'sudo docker exec -it <containerID> bash'
 
 ### End-points:
 #### basepath is /v2
 * /addString/{str} : This method will add the string from the query param to the data collection. and display the current collection of rows in the CSV.
  ``` 
  http://localhost:8080/v2/addString/String to added here
 
  #### Output:
  [{
  1,string
  },
  {
  2, row 2
  ...}]
   ```

* /fetchString/{id} : This method fetch the string by id and displays the row
  ``` 
  http://localhost:8080/v2/addString/2
  #### Output:
  {
  2, row 2
  }
   ``` 
