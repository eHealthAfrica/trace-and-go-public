# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from core.backends import sms_send_telerivet, sms_send_rapidpro  # noqa

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Usage MEDIA_ROOT = here('media')
here = lambda x: os.path.join(os.path.abspath(os.path.dirname(__file__)), x)


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'reversion',
    'reversion_compare',
    'djrill',
    'rest_framework',
    'rest_framework.authtoken',
    'core',
    'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'reversion.middleware.RevisionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'amsel.urls'

WSGI_APPLICATION = 'amsel.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tag',
        'USER': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

TEMPLATE_DIRS = (
    here('templates'),
)

STATIC_ROOT = here('../static_root')
STATIC_URL = '/static/'

MEDIA_ROOT = here('../media_root')
MEDIA_URL = '/media/'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "!@#THIS_IS_REALLY_SECURE!@#$%")

ALLOWED_HOSTS = []

# Rest Framework settings

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)

}

# This is a key that needs to be appended to the url when posting
# This is not really security but has become some sort of standard over
# the years. So if this is specified the post needs to be like:
# http://URL/submit?key=abc
# POST_KEY = "abc"


# Set the backend to send the sms
SMS_BACKEND = sms_send_rapidpro


COUNTRY_CODE = os.environ.get("COUNTRY_CODE", None)


# Set the auth key for you text.it account
# get it under http://textit.in
TEXTIT_AUT = os.environ.get("TEXTIT_AUT", "!@#THIS_IS_REALLY_SECURE!@#$%")

# Set the auth key for you rapidpro.io account
# get it under https://rapidpro.io/org/home/
RAPIDPRO_AUT = os.environ.get("RAPIDPRO_AUT", "!@#THIS_IS_REALLY_SECURE!@#$%")

# Telerivet REST API options
TE_API_KEY = os.environ.get("API_KEY", "!@#THIS_IS_REALLY_SECURE!@#$%")
TE_PROJECT_ID = os.environ.get("PROJECT_ID", "!@#THIS_IS_REALLY_SECURE!@#$%")

# Twilio REST API options
TW_SID = os.environ.get("TW_SID", "!@#THIS_IS_REALLY_SECURE!@#$%")
TW_AUTH = os.environ.get("TW_AUTH", "!@#THIS_IS_REALLY_SECURE!@#$%")

from local_settings import *  # noqa
