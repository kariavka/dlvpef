from django.utils.translation import ugettext_lazy as _
from admin_tools.dashboard import modules, Dashboard


class CustomAdminDashboard(Dashboard):
    """Custom admin panels."""

    def __init__(self, **kwargs):
        """ ... """
        Dashboard.__init__(self, **kwargs)

        # The site content group.
        content = modules.Group(
            title=_('Site manager').upper(),
            display='tabs',
            deletable=False,
            children=[
                modules.ModelList(
                    title=_('Feddabck'),
                    models=('audience.models.*', ),
                ),
                modules.ModelList(
                    title=_('Site content'),
                    models=('content.models.*', ),
                ),
            ]
        )

        # Django admin.
        manage = modules.Group(
            title=_('Administration').upper(),
            display='tabs',
            deletable=False,
            children=[
                modules.ModelList(
                    title=_('Users and Groups'),
                    models=('django.contrib.auth.models.User',
                        'django.contrib.auth.models.Group', ),
                ),
                modules.ModelList(
                    title=_('Sites'),
                    models=('django.contrib.sites.models.Site', ),
                ),
            ]
        )

        # Latest events on the site.
        recent_actions = modules.RecentActions(
            title=_('Recent Actions').upper(),
            column=2,
            collapsible=True,
            deletable=False,
            limit=10,
        )

        # Registration all groups.
        group_list = (content, manage, recent_actions, )
        for group in group_list:
            self.children.append(group)

