from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-(cg47_8n$8(0e58geuuu+r!kli-f2+-lbp*&sue_dzc9j#1$&3'

DEBUG = True



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
