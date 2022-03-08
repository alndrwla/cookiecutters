from configs.settings.base import *

import environ

ROOT_DIR = environ.Path(__file__) - 3

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

environ.Env.read_env(os.path.join(ROOT_DIR, ".envs/local"))

# Base
DEBUG = True

# Security
SECRET_KEY = env('SECRET_KEY',)

ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DATABASES["default"]["ATOMIC_REQUESTS"] = True

# Static js, css3

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, '../staticfiles/')

STATICFILES_DIRS = [os.path.join(BASE_DIR, '../static/')]

MEDIA_ROOT = os.path.join(BASE_DIR, '../mediafiles/')

MEDIA_URL = '/media/'
