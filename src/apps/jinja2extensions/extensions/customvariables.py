from django.conf import settings
from jinja2.ext import Extension

from jinja2extensions import apps


class CustomVariables(Extension):
    """This expansion allows to send in template the custom variables.

    Use the ``JINJA2EXTENSIONS_CUSTOM_VARIABLES`` dictionary in your
    ``settings.py`` to describe the custom variables.

    Example::

        # In settings.py
        JINJA2EXTENSIONS_CUSTOM_VARIABLES = {
            'GOOGLE_MAP_API_KEY': 'AIzaZyBnc7h_7I77NscpphRME_CeBdQNOfo7BE7',
        }

        # In your template
        <script src="https://maps.googleapis.com/maps/api/js?
            key={{ GOOGLE_MAP_API_KEY }}&signed_in=true&
            libraries=places&callback=initMap" async defer></script>

    """
    def __init__(self, environment):
        """Initialize globals."""
        super(CustomVariables, self).__init__(environment)

        for key, value in apps.CUSTOM_VARIABLES.items():
            environment.globals[key] = value

