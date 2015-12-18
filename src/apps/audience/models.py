from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Subscriber(models.Model):
    """Members who receive email notification when someone of the site users
    used the feedback.

    """
    full_name = models.CharField(
        max_length=30,
        blank=True,
        verbose_name=_('Full name'),
        help_text=_('The man\'s name for identification (not required).'),
    )
    email = models.EmailField(
        max_length=30,
        unique=True,
        verbose_name=_('E-mail'),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Active'),
    )

    class Meta:
        ordering = ('email', )
        verbose_name = _('subscriber')
        verbose_name_plural = _('Subscribers')


    def __str__(self):
        """The object is identified by e-mail."""
        return self.email


class Feedback(models.Model):
    """Messages that received from site users."""
    full_name = models.CharField(
        max_length=30,
        verbose_name=_('Full name'),
    )
    category = models.CharField(
        max_length=30,
        verbose_name=_('Category'),
    )
    subject = models.CharField(
        max_length=30,
        verbose_name=_('Subject'),
    )
    message = models.TextField(
        verbose_name=_('Message'),
    )

    # For a detailed report, we are using the timestamp.
    timestamp = models.DateTimeField(
        default=timezone.datetime.now,
        verbose_name=_('Date stamp'),
    )


    class Meta:
        ordering = ('category', 'timestamp', )
        verbose_name = _('message')
        verbose_name_plural = _('Messages')


    def __str__(self):
        """The object is identified by subject and full name."""
        return '{}: {}'.format(self.full_name, self.subject)

