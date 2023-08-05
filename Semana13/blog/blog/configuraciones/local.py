from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog_2db',
        'USER': 'root',
        'PASSWORD': 'rw-22.93-jg',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}