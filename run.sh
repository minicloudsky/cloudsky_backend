#!/bin/bash
echo "start stoping existed cloudsky-backend"
docker ps | grep cloudsky-backend | awk '{print $1}' | xargs docker stop
echo "start removing existed cloudsky-backend"
docker ps -a | grep cloudsky-backend | awk '{print $1}' | xargs docker rm
echo "start deploy cloudsky-backend"
docker run --name cloudsky-backend  -it -d -p 8000:8000  cloudsky-backend
