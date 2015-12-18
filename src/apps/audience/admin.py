from django.contrib import admin

from audience.models import Listener, Feedback


class ListenerAdmin(admin.ModelAdmin):
    """ ... """
    list_display = ('email', 'is_active', )
    search_fields = list_display
    list_display_links = list_display

    list_per_page = 20
    actions_on_top = True
    ordering = ('email', )

    save_on_top = True

    fieldsets = (
        (None, {
            'classes': ('full-width', ),
            'fields': ('email', 'is_active', ),
        }),
    )


class FeedbackAdmin(admin.ModelAdmin):
    """ ... """
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


admin.site.register(Listener, ListenerAdmin)
admin.site.register(Feedback, FeedbackAdmin)

