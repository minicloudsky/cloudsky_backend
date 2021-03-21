# coding=utf-8

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'mysql',
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


CACHES = {
    "default": {
         "BACKEND": "django_redis.cache.RedisCache",
         "LOCATION": "redis://redis:6379",
         "OPTIONS": {
             "CLIENT_CLASS": "django_redis.client.DefaultClient",
             "PASSWORD": ""
         }
     }
}
