# coding=utf-8
import os

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'root',
        'NAME': 'cloudsky_backend'
    },
    "test": {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'xxx.xxx.xxx.xxx',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'root',
        'NAME': 'root'
    }
}

IS_USE_OAUTH = True
OAUTH_URL = "http://10.4.168.228:8000"
OAUTH = {

    "BASE_URL": 'http://10.4.166.94:8063',
    "OAUTH_CLIENT_ID": '5Sf4s00xLbIuomIr5O2647usKy98PVby7ShJ9qhj',
    "OAUTH_CLIENT_SECRET": 'qGHcetfW8LxpfJQPJCT6nRBJfN9oPHIDtXyCvjrER39rjPZREgUWQWozEQuDlk2YiuOeS8DlbtbzwWbuu4BXbsfpKOm0HJwrfR0cF9mtTaf95XbjOFkryVLc5Mo45tub',
    "OAUTH_REDIRECT_URI": "http://10.4.166.94:8062/oauth/api-oauth-granted/",
    "OAUTH_AUTHENTICATE_TYPE": 'authorization_code',
    "OAUTH_AUTHENTICATE_URL": '%s/oauth2/authorize/' % OAUTH_URL,
    "OAUTH_TOKEN_URL": '%s/oauth2/token/' % OAUTH_URL,
    "OAUTH_ACCOUNT_URL": '%s/user/user_info' % OAUTH_URL,
    "OAUTH_CLIENT_STAFF": True,
    "JWT_VERITICATION_URL": "%s/api-token-verify/" % OAUTH_URL
}

IS_ALLOW_OAUTH_CREATE_USER = True
DEFALUT_USER_ROLE = []

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://xxx.xxx.xxx.xxx:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "xxxx"
        }
    }
}
