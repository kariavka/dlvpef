from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class Jinja2ExtensionsConfig(AppConfig):
    """The jinja2extensions settings."""
    name = 'jinja2extensions'
    verbose_name = _('Jinja2Extensions')

