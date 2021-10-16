#!/bin/bash
docker ps -a | grep cloudsky | awk '{print $1}' | xargs docker stop
docker ps -a | grep cloudsky | awk '{print $1}' | xargs docker rm
docker images | grep cloudsky | awk '{print $1}' | xargs docker rmi
