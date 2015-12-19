from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Page(models.Model):
    """Setting the content on the pages of the site."""
    ROLE_CHOICES = (
        ('main', _('Main page')),
        ('biography', _('Biography page')),
        ('information', _('Information page')),
        ('about', _('About page')),
    )
    role = models.CharField(
        max_length=16,
        unique=True,
        choices=ROLE_CHOICES,
        default='main',
        verbose_name=_('Role'),
        help_text=_('Page on the site.'),
    )

    title = models.CharField(
        max_length=256,
        verbose_name=_('Title'),
        help_text=_('On the main page, this field it is the slogan.'),
    )
    content = models.TextField(
        verbose_name=_('Content'),
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('Active'),
    )

    nav_title = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=_('Navigation title'),
        help_text=_('The text on the navigation button.'),
    )
    nav_role = models.CharField(
        max_length=512,
        blank=True,
        verbose_name=_('Navigation role'),
        help_text=_('Role of the navigation button - i.e., URL.'),
    )
    nav_is_active = models.BooleanField(
        default=True,
        verbose_name=_('Active navigation button'),
    )


    class Meta:
        ordering = ('id', )
        verbose_name = _('page')
        verbose_name_plural = _('Pages')


    def __str__(self):
        """The object is identified by title."""
        return self.title

