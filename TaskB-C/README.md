# Bubble Sort Technical Assignment

## Setting Up the Project
* Language [Python3](https://www.python.org/)
* [Ubuntu 20.04](https://ubuntu.com/)
* [Microsoft VS Code](https://code.visualstudio.com/)
* [Docker](https://docker.github.io/get-involved/docs/communityleaders/eventhandbooks/python/pythonapp/)
* [Postman](https://www.postman.com/downloads/)

## Running the app
In your terminal run the following commands:
* `docker build -t my-python-app .`
* `docker run -p 8000:5000 -it my-python-app`
* Open Postman
* In Postman, add the URL and change the type to POST. On the body tab, change to raw and select JSON from the drop-down. 
* POST http://172.17.0.2:5000/
  Body 
  raw JSON 
* Next, copy everythin in arr.json example into the text input.
* Send the request, and you should get the response. 

## Run unit tests
To run the unit test, run the following command in the terminal in folder TaskA and folder TaskB-C seperately:
* Run command `nox`
* Test configurations can be found in app_test.py.
* In order to run the tests, just type nox in the route and it will go through the test session and the linting session. Nox uses noxfile.py for all its session and confiugration. You will see two sections one for test and one for linting. It will also install the dependencies from requirements.txt.

### Questions
* #### Describe how your application performance is limited/bound by your available compute resources (I/O, CPU, Memory).
    *
* #### Describe how you would host the service and what considerations would be important to you.
    * My considerations for hosting the service would be a service that is fast and simple to deploy and affordable to host.
    * I would host the service on Docker because it has Github integration, allowing me to easily deploy my code with continuous integration.
* #### How long did this assignment take you and where did you spend your time?
    * The assignment took my about 7 hours to complete.
    * I took about an hour and half on the first two functions, flattening the nested arrays and then sorting the nested array. 
    * I then moved on to task B where I looked for the best framework I can use, of which I chose the Flask framework. I spent about more than an hour on this task.
    * My next step was installing Docker on my machine and migrating all the code I had written to the docker folder and making the necessary docker configurations.
    * The final task was writing the unit tests, and updating the Readme file.
    * Most of the time was used in research.
* #### What would you like to have done differently in your solutions above?
    * I would have preferred to have the ability to pass the json from a web front-end.