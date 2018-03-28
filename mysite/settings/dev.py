"""
Setting to be used strictly for development.
"""
from .base import *

DEBUG = True

INSTALLED_APPS = ['debug_toolbar',] + INSTALLED_APPS
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',] + MIDDLEWARE
INTERNAL_IPS = ['127.0.0.1', '0.0.0.0']






