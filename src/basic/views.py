from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    """Show homepage."""
    template_name = 'this/home.jinja'
