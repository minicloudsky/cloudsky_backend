#!/bin/bash
docker ps -a | grep cloud | awk '{print $1}' | xargs docker stop
docker ps -a | grep cloud | awk '{print $1}' | xargs docker rm
docker images | grep cloud | awk '{print $1}' | xargs docker rmi
