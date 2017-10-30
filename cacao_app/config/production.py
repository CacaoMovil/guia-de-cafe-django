# -*- coding: utf-8 -*-
'''
Production Configurations
'''
from os import environ
from configurations import values

from .common import Common


class Production(Common):
    # SECRET KEY
    SECRET_KEY = values.SecretValue()
    # END SECRET KEY

    # SITE CONFIGURATION
    # Hosts/domain names that are valid for this site
    # See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ["*"]
    # END SITE CONFIGURATION

    # See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html#settings
    # EMAIL
    DEFAULT_FROM_EMAIL = values.Value('cacao_app <info@example.com>')
    SERVER_EMAIL = values.Value(DEFAULT_FROM_EMAIL)
    EMAIL_HOST = values.Value('localhost')
    # END EMAIL

    # TEMPLATE CONFIGURATION
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
    #TEMPLATE_LOADERS = (
    #    ('django.template.loaders.cached.Loader', (
    #        'django.template.loaders.filesystem.Loader',
    #        'django.template.loaders.app_directories.Loader',
    #    )),
    #)
    # END TEMPLATE CONFIGURATION

    # CACHING
    # Only do this here because thanks to django-pylibmc-sasl and pylibmc
    # memcacheify is painful to install on windows.
    REDIS_DB = environ.get('DJANGO_REDIS_DB', '1')
    CACHES = {
        'default': {
            'BACKEND': 'redis_cache.RedisCache',
            'LOCATION': '127.0.0.1:6379',
            'OPTIONS': {
                'DB': REDIS_DB,
                'PARSER_CLASS': 'redis.connection.HiredisParser',
                'CONNECTION_POOL_CLASS': 'redis.BlockingConnectionPool',
                'CONNECTION_POOL_CLASS_KWARGS': {
                    'max_connections': 50,
                    'timeout': 20,
                }
            },
        },
    }
    # END CACHING

    # Your production stuff: Below this line define 3rd party libary settings

    PERSEUS_BUILD_DIR = '/tmp/ihcafe/build'
    PERSEUS_SOURCE_DIR = '/tmp/ihcafe/guia'
    USE_PERSEUS = False

    VENV_PATH = values.Value('/home/example/.virtualenvs/example')
