from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from audience.models import Subscriber, Feedback


class SubscriberAdmin(admin.ModelAdmin):
    """The admin panel for subscribers."""
    list_display = ('get_subscriber_data', 'is_active', )
    search_fields = list_display
    list_display_links = list_display

    list_per_page = 20
    actions_on_top = True
    ordering = ('email', )

    save_on_top = True

    fieldsets = (
        (None, {
            'classes': ('full-width', ),
            'fields': ('full_name', 'email', 'is_active', ),
        }),
    )

    def get_subscriber_data(self, obj):
        """Return subscriber data."""
        if obj.full_name:
            return '{} ({})'.format(obj.full_name, obj.email)
        return obj.email

    get_subscriber_data.short_description = _('Subscriber data')
    get_subscriber_data.admin_order_field = 'email'


class FeedbackAdmin(admin.ModelAdmin):
    """The admin panel for feedback."""
    list_display = ('category', 'subject', 'full_name', 'timestamp', )
    search_fields = list_display
    list_display_links = list_display

    list_per_page = 20
    actions_on_top = True
    ordering = ('timestamp', 'category', )

    save_on_top = True

    fieldsets = (
        (None, {
            'classes': ('full-width', ),
            'fields': ('category', 'subject', 'full_name', 'timestamp',
                'message', ),
        }),
    )

    readonly_fields = ('category', 'subject', 'full_name', 'timestamp',
        'message', )

    def has_add_permission(self, request):
        """..."""
        return False


# Register new models in Django admin.
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Feedback, FeedbackAdmin)

