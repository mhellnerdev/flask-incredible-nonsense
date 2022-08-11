#!/bin/sh

docker rm incrediblenonsense -f

docker rmi incrediblenonsense -f

docker image build -t incrediblenonsense .

docker run --name "incrediblenonsense" -d -p 5000:5000 incrediblenonsense