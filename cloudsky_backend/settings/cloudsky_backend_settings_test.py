# coding=utf-8

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
