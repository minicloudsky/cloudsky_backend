# coding=utf-8


import os

AUTH_MECHANISM = "GSSAPI"

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


EMAIL = {
    'sender': "",
    'user': '',
    'pwd': '',
    'smtp': 'smtp.xxx.com'
}

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
        'PASSWORD': 'xxxx',
        'NAME': 'test'
    }
}

DEFALUT_USER_ROLE = []


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://xxx.xxx.xxx.xxx:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": 'xxxx'
        }
    }
}
