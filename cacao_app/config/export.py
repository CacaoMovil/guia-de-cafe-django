'''
Django Perseus Config
'''
# -*- coding: utf-8 -*-
import os
from os.path import dirname

from .production import Production

BASE_DIR = dirname(dirname(__file__))

class Export(Production):
    USE_PERSEUS = True
    DEBUG = True
    SECRET_KEY = "lallamaquellama"
    THUMBNAIL_DEBUG = True
    RENDER_STATIC = True
    PERSEUS_BUILD_DIR = '/tmp/ihcafe/build'
    PERSEUS_SOURCE_DIR = '/tmp/ihcafe/guia'
    PERSEUS_STATIC_DIR = os.path.join(
        PERSEUS_SOURCE_DIR, "static"
    )
    PERSEUS_IMPORTERS = [
        'cacao.importers.MediaImporter',
        'cacao.importers.StaticImporter',
    ]
    MEDIA_URL = 'static/'
