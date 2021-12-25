# cloudsky_backend
## An easy to use and user-friendly microservice framework based on Django,deploy with gunicorn and docker.
### quickstart
```shell
docker pull minicloudsky/cloudsky-backend
```
```shell
docker run --name cloudsky-backend  -it -d -p 8000:8000  cloudsky-backend
```

### Api Test
#### Try to use postman or curl, send a request to  `http://your_host:8000/log/get_log/` ,then you will get the response as the following.
```json
{
  "code": 200,
  "msg": null,
  "data": {
    "page_num": 1,
    "page_size": 12,
    "total_size": 7,
    "total_pages": 1,
    "next": null,
    "content": [
      {
        "id": 1,
        "api_name": "/log/get_log/",
        "method": "GET",
        "param": "",
        "comment": "获取日志接口",
        "time": 283,
        "ip": "91.243.81.185",
        "create_time": "2021-12-25T18:36:09.834386+08:00",
        "username": "AnonymousUser",
        "status_code": "200",
        "status_text": "OK"
      }
    ]
  }
}
```
If you get the response like above,then your demo project is deployed success,enjoy~

### Usage
`git clone https://github.com/minicloudsky/cloudsky_backend.git`
1. write your business code,such as create your own apps,middlewares,then write tour django views,urls,models etc ...
2. Run `sh build.sh` to build a docker image.
3. Run `sh run.sh` to deploy your project, default `service port` is `8000`, you can edit the `Dockerfile` to customize your need.
### enjoy cloudsky-backend ~


