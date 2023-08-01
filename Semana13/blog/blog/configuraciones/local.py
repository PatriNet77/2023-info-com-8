from .settings import *

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