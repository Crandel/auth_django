from settings import  *
DEBUG=True

ALLOWED_HOSTS = ['kuddevurl.mykuwaitnet.net','159.253.153.37']
ADMINS = (
     ('Rajesh B K', 'rajeshbk042@gmail.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'kuddevur_server',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',
        'STORAGE_ENGINE':'MYISAM'
    }
}
