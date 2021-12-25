# cloudsky_backend
## An easy to use and user-friendly microservice framework based on Django,deploy with gunicorn and docker.
### quickstart
`docker pull minicloudsky/cloudsky-backend`
`docker run --name cloudsky-backend  -it -d -p 8000:8000  cloudsky-backend`
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
        "id": 7,
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
      },
      {
        "id": 6,
        "api_name": "/log/get_log/",
        "method": "GET",
        "param": "",
        "comment": "获取日志接口",
        "time": 306,
        "ip": "91.243.81.185",
        "create_time": "2021-12-25T18:27:22.633556+08:00",
        "username": "AnonymousUser",
        "status_code": "200",
        "status_text": "OK"
      },
      {
        "id": 5,
        "api_name": "/log/get_log/",
        "method": "GET",
        "param": "",
        "comment": "获取日志接口",
        "time": 54,
        "ip": "91.243.81.185",
        "create_time": "2021-12-25T18:22:51.254743+08:00",
        "username": "AnonymousUser",
        "status_code": "200",
        "status_text": "OK"
      },
      {
        "id": 4,
        "api_name": "/log/get_log/",
        "method": "GET",
        "param": "",
        "comment": "获取日志接口",
        "time": 271,
        "ip": "91.243.81.185",
        "create_time": "2021-12-25T18:22:44.810485+08:00",
        "username": "AnonymousUser",
        "status_code": "200",
        "status_text": "OK"
      },
      {
        "id": 3,
        "api_name": "/log/get_log/",
        "method": "GET",
        "param": "",
        "comment": "获取日志接口",
        "time": 73,
        "ip": "91.243.81.185",
        "create_time": "2021-12-25T18:20:52.703190+08:00",
        "username": "AnonymousUser",
        "status_code": "200",
        "status_text": "OK"
      },
      {
        "id": 2,
        "api_name": "/log/get_log/",
        "method": "GET",
        "param": "",
        "comment": "获取日志接口",
        "time": 367,
        "ip": "91.243.81.185",
        "create_time": "2021-12-25T18:20:45.826493+08:00",
        "username": "AnonymousUser",
        "status_code": "200",
        "status_text": "OK"
      },
      {
        "id": 1,
        "api_name": "/user/get/",
        "method": "GET",
        "param": "",
        "comment": "获取所有用户信息",
        "time": 124,
        "ip": "210.13.101.50",
        "create_time": "2021-03-23T18:23:54.896416+08:00",
        "username": "AnonymousUser",
        "status_code": "401",
        "status_text": "Unauthorized"
      }
    ]
  }
}
```
If you get the response like above,then your demo project is deployed success,enjoy~

### Usage
`git clone https://github.com/minicloudsky/cloudsky_backend.git`
### write your business code,such as create your own apps,middlewares,then write tour django views,urls,models etc ...
### Run `sh build.sh` to build a docker image.
### Run `sh run.sh` to deploy your project, default `service port` is `8000`, you can edit the `Dockerfile` to customize your need.


