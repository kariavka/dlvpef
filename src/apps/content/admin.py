from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from content.models import Page


class PageAdmin(admin.ModelAdmin):
    """The admin panel for site pages."""
    list_display = ('get_page_data', 'is_active', 'nav_is_active', )
    search_fields = list_display
    list_display_links = list_display

    list_per_page = 20
    actions_on_top = True
    ordering = ('role', )

    save_on_top = True

    fieldsets = (
        (None, {
            'classes': ('full-width', ),
            'fields': ('role', 'title', 'content', 'is_active', ),
        }),
        (_('Navigation'), {
            'classes': ('full-width', ),
            'fields': ('nav_title', 'nav_role', 'nav_is_active', ),
        }),
    )

    def get_page_data(self, obj):
        """Return page data."""
        return """
            <strong>{}</strong>: <em>{}</em><br/><br/>
            <span style="text-transform: uppercase;">{}</span>
            <p>{} ... </p>
            """.format(
                _('Role'),
                obj.get_role_display(),
                obj.title,
                obj.content[:128]
            )

    get_page_data.allow_tags = True
    get_page_data.short_description = _('Page data')
    get_page_data.admin_order_field = 'role'


# Register new models in Django admin.
admin.site.register(Page, PageAdmin)

