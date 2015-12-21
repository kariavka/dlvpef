"""Project URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))

"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import TemplateView

from solid_i18n.urls import solid_i18n_patterns

from basic import views
from basic import handlers


handler404 = handlers.PageNotFoundHandler.as_view()
handler500 = handlers.ServerErrorHandler.as_view()


# Localization URLS.
urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

# Admin URLS.
urlpatterns += [
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

# urlpatterns += i18n_patterns('',
urlpatterns += solid_i18n_patterns('',
    url(r'^$', views.HomeView.as_view(), name='home'),

    # System pages.
    url(r'^404.html$', handlers.PageNotFoundHandler.as_view(), name='e404'),
    url(r'^500.html$', handlers.ServerErrorHandler.as_view(), name='e500'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt',
        content_type='text/plain')),
)

# Static files.
# ** To run the project on the embedded server Django.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

