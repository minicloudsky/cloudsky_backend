FROM python:3.6
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt   --trusted-host mirrors.cloud.aliyuncs.com  -i http://mirrors.cloud.aliyuncs.com/pypi/simple/
RUN mkdir /tmp/cloudsky_backend
#CMD ["python", "init_database.py"]
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
#CMD ["python", "manage.py", "runserver", "0:8000"]

CMD ["gunicorn", "cloudsky_backend.wsgi:application", "--preload",  "-b", "0.0.0.0:8000", "-w", "5", "--log-level=debug",  "-c", "./gunicorn.py"]
