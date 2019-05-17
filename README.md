# MTCars Flask API

This is an API that uses the MTCars dataset and a linear regression model to predict `mpg` from the other remaining variables.

Everything is done with Python in a Docker container.

The `docker` folder contains everything necessary to build the Docker container.

The `scripts` folder contains the dataset and the Python scripts.

To use this API, first clone or download this repository and make sure Python 3.7 is installed and Docker is installed and running.

To run this API, open Terminal and change your directory to the docker folder.

Then run:

`docker-compose up`

If it has created the localhost server correctly you will not get your prompt back. As an initial test, open a new terminal in the same directory, and run the following curl command:

`curl http://localhost:5000/`

You should get the following response:

`The server is up.`

To predict `MPG` from the other variables, run a command of the following format:

`curl -H "Content-Type: application/json" -X POST -d '{"cyl":"6", "disp":"160", "hp":"110","draft":"3.7"}' "http://localhost:5000/mpg""`

The above command should produce the following result:

`{"mpg": 27.63627258279724}`

You can modify the variable values, and you can also adjust the number of cars for which you would like to predict the MPG. This example includes 1 car.

To stop your server running the API, type `ctrl-C`. Check to see if you have any docker containers running using `docker container ls`, and stop them through `docker container kill <container-name>`.

