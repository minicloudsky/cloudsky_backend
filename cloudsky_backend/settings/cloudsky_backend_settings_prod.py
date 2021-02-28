# coding=utf-8


import os

AUTH_MECHANISM = "GSSAPI"

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases



DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'mysql',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'root',
        'NAME': 'cloudsky_backend'
    },
}

DEFALUT_USER_ROLE = []


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": ''
        }
    }
}
