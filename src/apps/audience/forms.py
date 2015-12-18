from smtplib import SMTPAuthenticationError

from django import forms
from django.utils import timezone
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from audience.models import Feedback, Subscriber


class FeedbackForm(forms.ModelForm):
    """Feedback form."""
    class Meta:
        model = Feedback
        exclude = ('timestamp', )

    def save(self, *args, **kwargs):
        """When message is saved - inform all subscribers."""
        data = self.cleaned_data
        query = Q(is_active=True)
        subscribers = Subscriber.objects.filter(query).values_list('email')

        # Send notification to subscribers.
        if subscribers:
            # Title of message.
            message_title = '{}, {}'.format(
                data.get('full_name'),
                data.get('subject'),
            )

            # Message body.
            message_content = ('{timestamp_msg}: {timestamp}\n'
                '{category_msg}: {category}\n'
                '{message}').format(
                    timestamp_msg=_('Timestamp'),
                    timestamp=timezone.datetime.now(),
                    category_msg=_('Category'),
                    category=data.get('category'),
                    message=data.get('message'),
                )

            # Send mail.
            try:
                send_mail(
                    message_title,
                    message_content,
                    settings.EMAIL_HOST_USER,
                    [i[0] for i in subscribers],
                    fail_silently=False,
                )
            except SMTPAuthenticationError:
                pass

        return super(FeedbackForm, self).save(*args, **kwargs)

