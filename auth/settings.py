import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SECRET_KEY = 'g@hlp=xs^*y#2$8q3t+dzje7q@&7#@+82%zr^pr&@1a9ai=cl#'


DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.profile',
    'south',
    'social.apps.django_app.default',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]

ROOT_URLCONF = 'auth.urls'

WSGI_APPLICATION = 'auth.wsgi.application'

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookOAuth2',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'auth',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'STORAGE_ENGINE': 'MYISAM'
    }
}
LOGIN_URL = 'login/'
LOGOUT_URL = 'logout/'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'

AUTH_PROFILE_MODULE = 'apps.profile.'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

try:
    from local_settings import *
except:
    pass