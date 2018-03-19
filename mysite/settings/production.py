""" 
Settings to be used in production.
"""
import os
from .base import * 
SECRET_KEY = os.environ.get('SECRET_KEY', 'na!1i(grfayqf3sth=*h%yj2+z!q**t6@lfp_u365m!_%f=5ut')

DEBUG = False  

ALLOWED_HOSTS = [
    '127.0.0.1', 
    '0.0.0.0',
    ]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static_cdn")
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media_cdn")

SITE_NAME = "www.examplesite.com" #change when going live
PAGINATE_BY = 5

# Email settings
SPARKPOST_API_KEY = '79256ccb1c97835017433f1a336525b'
#EMAIL_BACKEND = 'sparkpost.django.email_backend.SparkPostEmailBackend'
EMAIL_HOST = 	'smtp.sparkpostmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'SMTP_Injection'
EMAIL_HOST_PASSWORD = SPARKPOST_API_KEY
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = "no-reply@examplesite.com"
