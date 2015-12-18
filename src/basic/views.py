from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy

from audience.forms import FeedbackForm


class HomeView(FormView):
    """Show homepage."""
    template_name = 'this/home.jinja'
    form_class = FeedbackForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        """Create new message."""
        response = super(HomeView, self).form_valid(form)
        form.save()
        return response

