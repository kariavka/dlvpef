"""
Django settings for DLVPEF project.

"""
import os
import sys

from django.utils.translation import ugettext_lazy as _
from django_jinja.builtins import DEFAULT_EXTENSIONS as \
    JINJA2_DEFAULT_EXTENSIONS


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# The root directory of the Django project.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# The root directory of the project (the lowest level).
BASE_DIR_UP = os.path.dirname(BASE_DIR)

# Path to the custom Django applications.
# ** It is necessary! If a third-party app is just copied to the apps/ but not
# installed through the pip.
sys.path.insert(1, os.path.join(BASE_DIR, 'apps'))

# Local server status.
DEBUG = True

# Applications.
INSTALLED_APPS = (
    # Admin tool's apps.
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',

    # Django.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # External apps.
    'captcha',

    # Custom apps.
    'jinja2extensions',
    'audience',
    'content',
)

# Project middleware.
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',

    'solid_i18n.middleware.SolidLocaleMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

# Templates (Jinja2 settings)
# The templates are found in custom applications too.
_template_dirs = [os.path.join(BASE_DIR, 'website/templates'), ]
for root, dirs, files in os.walk(os.path.join(BASE_DIR, 'apps')):
    if 'templates' in dirs:
        _template_dirs.append(os.path.join(root, 'templates'))

TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'APP_DIRS': True,
        'DIRS': _template_dirs,
        'OPTIONS': {
            # Match the template names ending in .html but not the ones in the
            # admin folder.
            'match_extension': ('.jinja', '.txt'),
            'match_regex': r'^(?!admin/).*',
            'app_dirname': 'templates',

            # Can be set to "jinja2.Undefined" or any other subclass.
            'undefined': None,
            'newstyle_gettext': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'extensions': JINJA2_DEFAULT_EXTENSIONS + \
                ['{}.{}'.format('jinja2extensions.extensions', i) for i in [
                    'builtinfunctions.BuiltInFunctionsExtension',
                    'localizations.LocalizationsExtension',
                    'customvariables.CustomVariables',
                    'djangocompatibility.CsrfExtension',
                    'djangocompatibility.DatetimeExtension',
                    'sorlthumbnail.SorlThumbnailExtension',
                ]],
            'filters': {
                'defaults': 'jinja2extensions.filters.classic.defaults',
                'nl2br': 'jinja2extensions.filters.classic.nl2br',
            },
            'autoescape': True,
            'auto_reload': DEBUG,
            'translation_engine': 'django.utils.translation',
        }
    },

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        # 'APP_DIRS': True, # No use if used loaders!!!
        'OPTIONS': {
            'context_processors': [
                'django.core.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'admin_tools.template_loaders.Loader',
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR_UP, 'world/var/sys/sqlite3/db.sqlite3'),
    }
}

# INTERNATIONALIZATION
# https://docs.djangoproject.com/en/1.8/topics/i18n/
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', _('English')),
    ('fr', _('France')),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR_UP, 'world/var/www/static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'website/static'),
)

# Media files (personal user's data).
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR_UP, 'world/var/www/media')

# Solid i18n.
SOLID_I18N_USE_REDIRECTS = True
SOLID_I18N_HANDLE_DEFAULT_PREFIX = False
SOLID_I18N_DEFAULT_PREFIX_REDIRECT = False
# JINJA2DJANGO_TRANSLATED_URL_HEAD_PREFIX = False

# Admin tools.
ADMIN_TOOLS_INDEX_DASHBOARD = 'basic.admintools.CustomAdminDashboard'
ADMIN_TOOLS_THEMING_CSS = 'admin/css/theming.css'

# Recaptcha.
# Add sites: diostim.com, dlvpef.org, weltwolke.com, 127.0.0.1, localhost
RECAPTCHA_PUBLIC_KEY = '6LcYiRMTAAAAAGTQiXgASzyl4Ait3u6-DqgZCQk8'
RECAPTCHA_PRIVATE_KEY = '6LcYiRMTAAAAAMYLRoxysBjxmPg3FPSlUWrRekHM'
NOCAPTCHA = True

