from django.contrib import admin

from audience.models import Listener


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

admin.site.register(Listener, ListenerAdmin)

