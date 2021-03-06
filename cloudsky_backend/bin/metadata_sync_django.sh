#!/usr/bin/env bash


PROJECT_PATH=/home/project/cloudsky_backend
PYTHON_PATH=python


python $PROJECT_PATH/manage.py  makemigrations
python $PROJECT_PATH/manage.py  migrate
python $PROJECT_PATH/manage.py  collectstatic