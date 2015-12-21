from django.db.models import Q
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy

from audience.forms import FeedbackForm
from content.models import Page, Information


class HomeView(FormView):
    """Show homepage."""
    template_name = 'this/home.jinja'
    form_class = FeedbackForm
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        """Get context data."""
        context = super(HomeView, self).get_context_data(*args, **kwargs)

        query = Q(is_active=True)
        pages = Page.objects.filter(query)
        context['pages'] = {obj.role:obj for obj in pages}
        context['information'] = Information.objects.last()

        return context

    def form_valid(self, form):
        """Save message and inform all subscribers."""
        response = super(HomeView, self).form_valid(form)
        form.save()
        return response

