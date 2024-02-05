from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'admin1234'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sistema_autos',
        'USER': 'divto',
        'PASSWORD': 'divtopc27',
        'HOST': 'localhost',
        'PORT': '5432',
        
    }
}