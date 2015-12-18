from django import forms
from django.db.models import Q

from audience.models import Feedback, Subscriber


class FeedbackForm(forms.ModelForm):
    """Feedback form."""
    class Meta:
        model = Feedback
        exclude = ('timestamp', )

    def save(self, *args, **kwargs):
        """When message is saved - inform all subscribers."""
        subscribers = Subscriber.objects.filter(Q(is_active=True))
        # Infrom subscribers here...

        return super(FeedbackForm, self).save(*args, **kwargs)

