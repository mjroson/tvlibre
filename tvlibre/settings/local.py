from .base import *


DEBUG = True

TEMPLATE_DEBUG = DEBUG


# INSTALLED_APPS += (
#     'django_extensions',   # for Ipython Notebook
#     'debug_toolbar',
#
# )
SITE_ID = 1
# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}