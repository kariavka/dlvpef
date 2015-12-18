"""
Additional application settings that can be changed in your ``settings.py``.

P.S. For all settings, use the ``JINJA2EXTENSIONS_`` prefix.

"""
from django.conf import settings

# SYSTEM
# The initialization function. Get attribute from settings, if not possible -
# get the default data. Add for all attributes a prefix as app name.
APP_PREFIX = 'JINJA2EXTENSIONS_'
init = lambda attr, default=None: getattr(settings, APP_PREFIX + attr, default)


# TRANSLATED_URL_HEAD_PREFIX
# If is ``True`` used in the URL language code for the language even default.
TRANSLATED_URL_HEAD_PREFIX = init('TRANSLATED_URL_HEAD_PREFIX', True)

# CUSTOM VARIABLES
# Accepts dictionary that you want to transfer into all templates.
CUSTOM_VARIABLES = init('CUSTOM_VARIABLES', {})

