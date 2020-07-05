# -*- coding: utf-8 -*-
# @File  : local.py
# @Author: clelandgt@163.com
# @Date  : 2020-07-04
# @Desc  :
from fresh_shop.settings.common import *


# Python
PYTHON_INTERPRETER = '/Users/cleland/.pyenv/versions/3.7.1/envs/base/bin/python'


# 数据库
META_STORE_DB = 'fresh_shop'
META_STORE_HOST = 'localhost'
META_STORE_PORT = 3306
META_STORE_USER = 'root'
META_STORE_PASSWORD = 'ganZHEyu'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
import pymysql
pymysql.version_info=(1,3,13,"final",0)
pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': META_STORE_DB,
        'USER': META_STORE_USER,
        'PASSWORD': META_STORE_PASSWORD,
        'HOST': META_STORE_HOST,
        'PORT': META_STORE_PORT
    }
}
# 账号 cleland  密码: Cleland123!

# # Django的缓存配置
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }


CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': [
            '127.0.0.1:6379',
        ],
        'OPTIONS': {
            'DB': 2,
            #'PASSWORD': 'yadayada',
            'PARSER_CLASS': 'redis.connection.HiredisParser',
            'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
            'CONNECTION_POOL_CLASS_KWARGS': {
                'max_connections': 50,
                'timeout': 20,
            },
            'MAX_CONNECTIONS': 1000,
            'PICKLE_VERSION': -1,
        },
    },
}

# email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'clelandgt@163.com'
EMAIL_HOST_PASSWORD = 'HRDGCNJRTBCOFIPK'
EMAIL_FROM = 'clelandgt@163.com'