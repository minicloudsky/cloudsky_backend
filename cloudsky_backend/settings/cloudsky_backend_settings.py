# coding=utf-8
import os

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'aliyun.yawujia.cn',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'root',
        'NAME': 'cloudsky_backend'
    },
    # "test": {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'HOST': 'xxx.xxx.xxx.xxx',
    #     'PORT': 3306,
    #     'USER': 'root',
    #     'PASSWORD': 'root',
    #     'NAME': 'test'
    # }
}

DEFALUT_USER_ROLE = []

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#             "PASSWORD": "xxxx"
#         }
#     }
# }
