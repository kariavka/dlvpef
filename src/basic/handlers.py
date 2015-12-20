import django

from django.conf import settings
from django.views.generic import View
from django.template import loader, RequestContext
from django import http


class GenericHandler(View):
    """Generic Handler."""
    response_cls = http.HttpResponse
    content_type = "text/html"
    tmpl_name = None

    def get_context_data(self):
        """..."""
        return {'view': self}

    def get(self, request, *args, **kwargs):
        """..."""
        context = self.get_context_data()
        if django.VERSION[:2] < (1, 8):
            output = loader.render_to_string(self.tmpl_name, context,
                context_instance=RequestContext(request))
        else:
            output = loader.render_to_string(self.tmpl_name, context,
                request=request)

        return self.response_cls(output, content_type=self.content_type)


class PageNotFoundHandler(GenericHandler):
    """Page Not Found Handler."""
    tmpl_name = '404.jinja'
    response_cls = http.HttpResponseNotFound


class ServerErrorHandler(GenericHandler):
    """Server Error Handler."""
    tmpl_name = '500.jinja'
    response_cls = http.HttpResponseServerError

