from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from content.models import Page, Information


class PageAdmin(admin.ModelAdmin):
    """The admin panel for site pages."""
    list_display = ('get_page_data', 'is_active', 'nav_is_active', )
    search_fields = list_display
    list_display_links = list_display

    list_per_page = 20
    actions = ('delete_action', 'activate_action', 'deactivate_action', )
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

    # Actions manager.
    def get_actions(self, request):
        """Remove some of the standard actions."""
        actions = super(PageAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']

        return actions

    def delete_action(self, request, objects):
        """Delete selected entries."""
        for obj in objects.all():
            obj.delete()

        super(PageAdmin, self).delete_model(request, objects)

    delete_action.short_description = _('Delete selected entries')

    def activate_action(self, request, objects):
        """Activate selected entries."""
        for obj in objects.all():
            obj.is_active = True
            obj.save()

    activate_action.short_description = _('Activate selected entries')

    def deactivate_action(self, request, objects):
        """Deactivate selected entries."""
        for obj in objects.all():
            obj.is_active = False
            obj.save()

    deactivate_action.short_description = _('Deactivate selected entries')


class InformationAdmin(admin.ModelAdmin):
    """The admin panel for site informations."""
    list_display = ('title', )
    search_fields = list_display
    list_display_links = list_display

    list_per_page = 20
    actions = ('delete_action', )
    actions_on_top = True
    ordering = ('id', )

    save_on_top = True

    fieldsets = (
        (_('Page'), {
            'classes': ('full-width', ),
            'fields': ('title', ),
        }),
        (_('Feedback'), {
            'classes': ('full-width', ),
            'fields': ('feedback_title', 'feedback_content',
                'feedback_is_active', ),
        }),
        (_('SEO'), {
            'classes': ('full-width', ),
            'fields': ('seo_title', 'seo_keywords', 'seo_description', ),
        }),
    )


    def has_add_permission(self, *args, **kwargs):
        """There should be stored only one entry."""
        return False if Information.objects.count() > 0 else True


    # Actions manager.
    def get_actions(self, request):
        """Remove some of the standard actions."""
        actions = super(InformationAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']

        return actions

    def delete_action(self, request, objects):
        """Delete selected entries."""
        for obj in objects.all():
            obj.delete()

        super(InformationAdmin, self).delete_model(request, objects)

    delete_action.short_description = _('Delete selected entries')


# Register new models in Django admin.
admin.site.register(Page, PageAdmin)
admin.site.register(Information, InformationAdmin)


