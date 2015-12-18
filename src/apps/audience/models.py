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

