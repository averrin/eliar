# -*- coding: utf-8 -*-
# Django settings for eliar project.

import os, sys
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
('Averrin', 'averrin@gmail.com'),
)
INTERNAL_IPS = ('127.0.0.1', '77.239.247.102')

DEFAULT_CHARSET = 'utf-8'
FILE_CHARSET = 'utf-8'
MANAGERS = ADMINS


PROJECT_DIR = os.path.dirname(__file__)
sys.path.append(PROJECT_DIR)

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_DIR,'eliar.db'), # Or path to database file if using sqlite3.
        'USER': '', # Not used with sqlite3.
        'PASSWORD': '', # Not used with sqlite3.
        'HOST': '', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
)
LOCALE_PATHS=(os.path.dirname(__file__))

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin-media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'o@pd=w^=1-39kwqo25p9_w1+a4#^2ub#u!@=23cto10165*3t-'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
('django.template.loaders.cached.Loader', (
'django.template.loaders.filesystem.Loader',
'django.template.loaders.app_directories.Loader',
)),
)

MIDDLEWARE_CLASSES = (
'django.middleware.common.CommonMiddleware',
'django.contrib.sessions.middleware.SessionMiddleware',
#'django.middleware.csrf.CsrfViewMiddleware',
'django.contrib.auth.middleware.AuthenticationMiddleware',
'django.contrib.messages.middleware.MessageMiddleware',
'debug_toolbar.middleware.DebugToolbarMiddleware',
'middlewares.SwitchLocaleMiddleware',
'subdomains.middleware.SubdomainURLRoutingMiddleware',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

TEMPLATE_CONTEXT_PROCESSORS += (
"django.core.context_processors.i18n",
'django.core.context_processors.request',
'shared.my_context',
)

ROOT_URLCONF = 'eliar.urls'



TEMPLATE_DIRS = (
# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
os.path.join(PROJECT_DIR, 'templates'),
)

PROJECT_APPS = (
'main',
'dev_tools',
'accounts',
'portfolio',
'blog',
'mish',
'areal'
)

INSTALLED_APPS = (
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.sites',
'django.contrib.messages',
'grappelli',
'registration',
'my_invitation',
'django_assets',
'messages',
'rosetta',
'inplaceeditform',
'django_extensions',
'django_jenkins',
'debug_toolbar',
'django.contrib.admin',
)
INSTALLED_APPS += PROJECT_APPS

MEDIA_URL = STATIC_URL = '/static/'
MEDIA_ROOT = STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

ASSET_URL = '/static/gen/'
ASSET_ROOT = os.path.join(STATIC_ROOT, 'gen')

ADMIN_MEDIA_ROOT = os.path.join(STATIC_ROOT, 'admin-media')
ADMIN_MEDIA_URL = '/admin-media/'
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
            },
        }
}

ACCOUNT_INVITATION_DAYS = 14
INVITATIONS_PER_USER = 0
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'averrin.dev@googlemail.com'
EMAIL_HOST_PASSWORD = 'charmium'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'averrin.dev@googlemail.com'
INVITE_MODE = True
ACCOUNT_ACTIVATION_DAYS = 14
DEBUG_TOOLBAR_CONFIG={"INTERCEPT_REDIRECTS":False}

AUTH_PROFILE_MODULE = 'accounts.UserProfile'

ROOT_URLCONF = 'eliar.urls'

SUBDOMAIN_URLCONFS = {
    # The format for these is 'subdomain': 'urlconf'
    None: 'eliar.urls',
    'www': 'eliar.urls',
    'me': 'eliar.main.me_urls',
    'blog': 'eliar.main.blog_urls',
    }

try:
    f = open(os.path.join(PROJECT_DIR, 'ver'), 'r')
    VERSION = f.read()
    f.close()
except:
    VERSION = ''

try:
    from local_settings import *
except ImportError:
    pass
