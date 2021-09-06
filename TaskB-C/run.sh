#!/bin/bash

echo "Welcome to Asa's bubble sort Offerzen Technical Assignment"

date

echo "Running unit tests"
nox
echo "Running Docker... Please put in your sudo password"
echo "After that please open Postman and follow the instructions"
sudo docker build -t my-python-app .
sudo docker run -p 8000:5000 -it my-python-app

echo "Please open Postman and follow the instructions"