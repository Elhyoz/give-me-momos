from momos.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('MOMOS_DB_NAME'),
        'USER': os.getenv('MOMOS_DB_USER'),
        'PASSWORD': os.getenv('MOMOS_DB_PASSWORD'),
        'HOST': os.getenv('MOMOS_DB_HOST'),
        'PORT': os.getenv('MOMOS_DB_PORT'),
    }
}

STATIC_ROOT = 'staticfiles'

MEDIA_URL= '/'
