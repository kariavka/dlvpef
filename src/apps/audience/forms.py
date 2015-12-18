from django import forms

from audience.models import Feedback


class FeedbackForm(forms.ModelForm):
    """..."""
    class Meta:
        model = Feedback
        exclude = ('timestamp', )

