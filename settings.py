# Django settings for secretteatours project.

import os
PROJECT_PATH = os.path.normpath(os.path.dirname(__file__))


# GENERAL SETTINGS
# ----------------------------------

DEBUG = False
THUMBNAIL_DEBUG = True
TEMPLATE_DEBUG = DEBUG
GA_IS_ON = True
PROJECT_NAME = 'Secret Tea Tours'
PROJECT_WEBSITE = 'secretteatours.com'
ADMINS = (
    ('Chris West', 'chris@minrivertea.com'),
    ('Bethan Thomas', 'bethan@email.com')
)
MANAGERS = ADMINS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


# LOCALE AND LANGUAGE TYPE SETTINGS
# -------------------------------------

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-gb'
SITE_ID = 1
USE_I18N = False
USE_L10N = False


# Media and static file settings
# ---------------------------------------


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

THUMB_LARGE = '400x310'
THUMB_MEDIUM = '210x160'
THUMB_SMALL = '80x80'

# Template settings
# -----------------------------------------


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, "templates/"),
)

BASE_TEMPLATE = 'base.html'

TEMPLATE_CONTEXT_PROCESSORS = (
     'django.core.context_processors.request',
     'django.contrib.auth.context_processors.auth',
     'context_processors.common',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'website',
    'sorl.thumbnail',
)


try:
    from local_settings import *
except:
    pass
