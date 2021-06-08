from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-(cg47_8n$8(0e58geuuu+r!kli-f2+-lbp*&sue_dzc9j#1$&3'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', '']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_control',
        'USER': 'dj_admin',
        'PASSWORD': 'qwerty123',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')