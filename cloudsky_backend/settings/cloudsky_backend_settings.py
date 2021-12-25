# coding=utf-8

DATABASES = {
    # "default": {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
    # },
    "default": {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'aliyun.yawujia.cn',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': 'root',
        'NAME': 'cloudsky_backend'
    }
}

"""
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
"""
