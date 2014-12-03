# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from core.backends import sms_send_telerivet

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

STATIC_URL = '/static/'

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.staticfiles',    
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'south',
    'core',
    'djrill',
    'etu',
    'rest_framework',
    'rest_framework.authtoken'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',

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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

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
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
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
#POST_KEY = "abc"

# You can set the method that should be used to evaluate your
# json here.
from core.eval_methods import eval_json
EVAL_METHOD = eval_json
#This could also be a list of methods if you want to evaluate more than one
#EVAL_METHOD = [eval_json, eval_json2]


#Set the backend to send the sms
SMS_BACKEND = sms_send_telerivet

# Set the auth key for you text.it account
# get it under http://textit.in
TEXTIT_AUT = os.environ.get("TEXTIT_AUT", "!@#THIS_IS_REALLY_SECURE!@#$%")

#Telerivet REST API options
TE_API_KEY = os.environ.get("API_KEY", "!@#THIS_IS_REALLY_SECURE!@#$%")
TE_PROJECT_ID = os.environ.get("PROJECT_ID", "!@#THIS_IS_REALLY_SECURE!@#$%")

#Twilio REST API options
TW_SID = os.environ.get("TW_SID", "!@#THIS_IS_REALLY_SECURE!@#$%")
TW_AUTH  = os.environ.get("TW_AUTH", "!@#THIS_IS_REALLY_SECURE!@#$%")
