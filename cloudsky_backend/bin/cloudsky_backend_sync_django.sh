#!/usr/bin/env bash


PROJECT_PATH=$(cd "$(dirname "$0")"; cd ../;pwd)
PYTHON_PATH=python


python $PROJECT_PATH/manage.py  makemigrations
python $PROJECT_PATH/manage.py  migrate
python $PROJECT_PATH/manage.py  collectstatic