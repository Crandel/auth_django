"""
Django settings for kud project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
gettext = lambda s: s
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.abspath(os.path.join(BASE_DIR, os.path.pardir))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yisbp)(an*d997urz8h)grlqsvxsh)^0d!p*-asm@f-qm68bew'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SITE_ID=1

THUMBNAIL_DEBUG=True



ROOT_URLCONF = 'kud.urls'

WSGI_APPLICATION = 'kud.wsgi.application'


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


LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('en', 'English'),
    ('ar', 'Arabic'),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Application definition

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'modeltranslation',
    'cms',
    'mptt',
    'menus',
    'south',
    'sekizai',
    'sorl.thumbnail',
    'ckeditor',
    'captcha',
    'inline_ordering',
    'import_export',
    'haystack',
    'robots',
    'django_mailer',
    'endless_pagination',
    'django_extensions',
#    'mailer',
    'apps.home',
    'apps.general',
    'apps.project',
    'apps.contactus',
    'apps.contact_plugin',
    'apps.flatpages',
    'django.contrib.flatpages',
    'apps.newsevents',
    'apps.careers',
    'apps.gallery_plugin',
    'apps.xmlsitemap',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'sekizai.context_processors.sekizai',
    'cms.context_processors.cms_settings',
)

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'staticfiles'),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_DIRS = (
    # The docs say it should be absolute path: PROJECT_PATH is precisely one.
    # Life is wonderful!
    os.path.join(BASE_DIR, "templates"),
)

TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',)

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {

   'default': {
       'toolbar': [
           [ 'Source','','Save','NewPage','DocProps','Preview','Print','','Templates' ],
           [ 'Cut','Copy','Paste','PasteText','PasteFromWord','-','Undo','Redo' ] ,
           [ 'Find','Replace','','SelectAll','','SpellChecker', 'Scayt' ],
           [ 'Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
       'HiddenField' ],
       [ 'Bold','Italic','Underline','Strike','Subscript','Superscript','-','RemoveFormat' ],
        [ 'NumberedList','BulletedList','','Outdent','Indent','','Blockquote','CreateDiv',
       '','JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock','','BidiLtr','BidiRtl' ],
       [ 'Link','Unlink','Anchor' ],
        [ 'Image','Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak','Iframe' ],
        [ 'Styles','Format','Font','FontSize' ],
         [ 'TextColor','BGColor' ],
          [ 'Maximize', 'ShowBlocks','-','About' ],
       ],

   },
}


RECAPTCHA_PUBLIC_KEY = '6Lege_0SAAAAAAKrgrHMljvqw55RyoLKU_8rPEoY'
RECAPTCHA_PRIVATE_KEY = '6Lege_0SAAAAAIIFMuxMJbuZPPYpWJYuHRHUFLdj'
RECAPTCHA_USE_SSL = True


CMS_TEMPLATES = (
    ('home.html', 'Home'),
    ('aboutus.html', 'About US'),
    ('ourservices.html', 'Our Services'),
    ('portfolio.html', 'Portfolio'),
    ('portfolio_detail.html', 'Portfolio Detail'),
    ('career_page.html', 'Career PAge'),
    ('news.html', 'News'),
    ('contactus/contact.html', 'Contact Us'),
    ('subsidiaries/subsidiaries.html', 'Subsidiaries'),

)

CMS_PLACEHOLDER_CONF = {
        'contactaddress':{
        "plugins": ('ContactAddressPlugin'),
        "name": gettext('Contact Address Plugin')
    },



      'imagegallery':{
        "plugins": ('CMSGalleryPlugin'),
        "name": gettext('Image Gallery')
    },
}

ACCEPTED_CV_FORMATS=['doc','pdf','jpg','jpeg',]
#CKEDITOR_IMAGE_BACKEND='pillow'

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}


HAYSTACK_SEARCH_RESULTS_PER_PAGE=1
