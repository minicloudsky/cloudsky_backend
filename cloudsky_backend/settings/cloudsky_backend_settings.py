# coding=utf-8
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://01d50b0f8c0d42dd83b62316f57f4e5c@o536107.ingest.sentry.io/5654644",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True
)

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
