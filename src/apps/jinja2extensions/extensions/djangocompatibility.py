"""
Extensions for compatibility with django.
"""
from django.utils import timezone
from django.contrib import messages

from jinja2 import nodes
from jinja2 import Markup
from jinja2.ext import Extension


class CsrfExtension(Extension):
    """Using the ``{% csrf token %}`` tag for the rapid publication for
    protection in the HTML form.

    """
    tags = set(['csrf_token'])

    def __init__(self, environment):
        self.environment = environment

    def parse(self, parser):
        lineno = parser.stream.expect('name:csrf_token').lineno
        call = self.call_method(
            '_render',
            [nodes.Name('csrf_token', 'load', lineno=lineno)],
            lineno=lineno
        )

        return nodes.Output([nodes.MarkSafe(call)])

    def _render(self, csrf_token):
        if csrf_token:
            if csrf_token == 'NOTPROVIDED':
                return Markup("")

            return Markup('<input type="hidden" name="csrfmiddlewaretoken" '
                'value="{}" />'.format(csrf_token))

        if settings.DEBUG:
            import warnings
            warnings.warn('A {% csrf_token %} was used in a template, but the '
                'context did not provide the value.  This is usually caused '
                'by not using RequestContext.')

        return ''


class DatetimeExtension(Extension):
    """..."""
    tags = set(['now'])

    def __init__(self, environment):
        environment.globals['now'] = self._now()

    def parse(self, parser):
        lineno = parser.stream.expect('name:now').lineno
        call = self.call_method('_render')
        return nodes.Output([nodes.MarkSafe(call)])

    def _render(self):
        return Markup(timezone.datetime.now())


    def _now(self):
        return timezone.datetime.now()

