
from settings import  *
DEBUG=False

ALLOWED_HOSTS = ['kuddevurl.mykuwaitnet.net']
ADMINS = (
     ('Rajesh B K', 'rajeshbk042@gmail.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kuddevur_server',
        'USER': 'kuddevur_dev',
        'PASSWORD': ']FiGg0}ZA[U8',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',
        'STORAGE_ENGINE':'MYISAM'
    }
}


EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'tester@kuwaitnet'
EMAIL_HOST_USER     = 'tester.kuwaitnet@gmail.com'
EMAIL_ADMIN         = 'tester.kuwaitnet@gmail.com'
EMAIL_PORT          =  587
EMAIL_USE_TLS       =  True
DEFAULT_FROM_EMAIL  = 'tester.kuwaitnet@gmail.com'

EMAIL_BACKEND = "django_mailer.smtp_queue.EmailBackend"

try:
    from local_settings import *
except:
    pass
