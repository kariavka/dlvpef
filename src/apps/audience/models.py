from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Listener(models.Model):
    """ ... """
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
        verbose_name = _('listener')
        verbose_name_plural = _('Listeners')


    def __src__(self):
        """ ... """
        return self.email


class Feedback(models.Model):
    """..."""
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

    timestamp = models.DateTimeField(
        default=timezone.datetime.now,
        verbose_name=_('Date stamp'),
    )


    class Meta:
        ordering = ('category', 'timestamp', )
        verbose_name = _('message')
        verbose_name_plural = _('Messages')


    def __src__(self):
        """ ... """
        return self.subject

