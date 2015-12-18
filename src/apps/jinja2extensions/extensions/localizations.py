from django.http import Http404
from django.conf import settings
from django.core.urlresolvers import resolve, reverse
from django.utils.translation import activate, get_language_info, get_language

from jinja2.ext import Extension

from jinja2extensions import apps


class LocalizationsExtension(Extension):
    """Register additional tags for easy work with localization.

    CONSTANTS

        LANGUAGES
            The tuple of the available languages, based on the
            ``settings.LANGUAGES``.

        LANGUAGE_CODE
            The current language code (it is not ``settings.LANGUAGE_CODE``).
            You can use in the template ``{{LANGUAGE_CODE}}`` to find out what
            language is selected for site interface.

        LANGUAGE_CODE_DEFAULT
            The language code that in the system set by default (it is
            ``settings.LANGUAGE_CODE``).


    EXTENSIONS

        get_language_info
            The extension provides detailed information about languages (read
            `about get_language_info`_).

            Example::

                {% set language_info 'en'|get_language_info %}
                Language info: {{ get_language_info('en') }}
                {% for language_code, language_name in LANGUAGES %}
                    {{ language_name }}: {{ language_code|get_language_info }}
                {% endfor %}

        get_translated_url
            The extension gets the current URL and converts it to a translated
            URL based on the selected language.

            Example::

                {% set next = '/en/about/'|get_translated_url('ru') %}
                Next: {{ get_translated_url('/en/about/', 'ru') }}


    SETTINGS

        In order to properly use the extension of LocalizationsExtension - you
        need to configure your application. You can customize the application
        without having to install external packages. And also make more
        beautiful the URL by installing the ``django-solid-i18n-urls``.

        STANDART DJANGO SETTINGS

        :See also: `Language prefix in URL patterns`_

        urls.py ::

            from django.conf.urls.i18n import i18n_patterns

            urlpatterns = [
                url(r'^i18n/', include('django.conf.urls.i18n')),
            ]

            urlpatterns += i18n_patterns('',
                url(r'^$', views.Home.as_view(), name='home'),
            )

        settings.py ::

            MIDDLEWARE_CLASSES += (
                'django.middleware.locale.LocaleMiddleware',
            )


        SETTINGS WITH ``django-solid-i18n-urls``

        :See also: `django-solid-i18n-urls`_

        urls.py ::

            from solid_i18n.urls import solid_i18n_patterns

            urlpatterns = [
                url(r'^i18n/', include('django.conf.urls.i18n')),
            ]

            urlpatterns += solid_i18n_patterns('',
                url(r'^$', views.Home.as_view(), name='home'),
            )

        settings.py ::

            MIDDLEWARE_CLASSES += (
                'solid_i18n.middleware.SolidLocaleMiddleware',
            )

            SOLID_I18N_USE_REDIRECTS = True
            JINJA2EXTENSIONS_TRANSLATED_URL_HEAD_PREFIX = False

    .. ..................................................................... ..
    .. _`about get_language_info`:
        https://docs.djangoproject.com/en/1.8/topics/i18n/translation/
            #django.utils.translation.get_language_info

    .. _`Language prefix in URL patterns`:
        https://docs.djangoproject.com/en/1.8/topics/i18n/translation/
            #language-prefix-in-url-patterns
    .. _`django-solid-i18n-urls`:
        https://github.com/st4lk/django-solid-i18n-urls


    """
    def __init__(self, environment):
        """ ... """
        super(LocalizationsExtension, self).__init__(environment)

        # CONSTANTS
        # * LANGUAGES - tuple of the available languages, based on the
        # `settings.LANGUAGES` data.
        environment.globals['LANGUAGES'] = settings.LANGUAGES
        environment.globals['LANGUAGE_CODE'] = self._get_language_code()
        environment.globals['LANGUAGE_CODE_DEFAULT'] = settings.LANGUAGE_CODE

        environment.globals['get_language_info'] = self._get_language_info
        environment.filters['get_language_info'] = self._get_language_info

        environment.globals['get_translated_url'] = self._get_translated_url
        environment.filters['get_translated_url'] = self._get_translated_url


    def _get_language_code(self):
        """Define a language code that is selected in the system."""
        # In order to obtained the language code as the constant in template
        # (i.e. {{ LANGUAGE_CODE }}, bat not as {{ LANGUAGE_CODE() }} - call
        # method), we perform wrapper `get_language` method call through a
        # `__repr__` class method.
        class LanguageCode(object):
            def __repr__(self):
                return get_language()

        # Get object.
        return LanguageCode()


    def _get_language_info(self, langusge_code):
        """The get_language_info() function provides detailed information about
        languages.

        """
        return get_language_info(langusge_code)


    def _get_translated_url(self, path, language_code='en'):
        """The method return the current URL and converts it to a translated
        URL based on the selected language.

        """
        # Determine the GET query.
        query = ''
        if '?' in path:
            path, query = path.split('?', 1)

        try:
            # Try to get information about the specified path.
            url_data = resolve(path)
        except Http404:
            try:
                # Try to get data about the root path.
                url_data = resolve('/')
            except Http404:
                # Determine whether the prefixed language URL when selecting
                # the default language.
                url_head_prefix = apps.TRANSLATED_URL_HEAD_PREFIX

                # If selected the current language and the prefix is not
                # needed.
                if language_code == settings.LANGUAGE_CODE:
                    if not url_head_prefix:
                        return '/'

                # If the specified language in the list of permitted - write it
                # as a URL prefix.
                if language_code in [i[0] for i in settings.LANGUAGES]:
                    return '/{}/'.format(language_code)

                return '/'

        # If access to the patterns indicated by through namespaces.
        url_name = '{}'
        if url_data.namespaces:
            url_name = '{}:{{}}'.format(':'.join(url_data.namespaces))

        url_name = url_name.format(url_data.url_name)

        # To determine the current language code.
        current_language_code = get_language()

        # Activate the specified language.
        activate(language_code)

        # Define a new path based on the specified language.
        url_path = reverse(url_name, args=url_data.args,
            kwargs=url_data.kwargs)

        # Activate the current language.
        activate(current_language_code)

        # Return the path and GET query.
        return url_path + ('' if not query else '?' + query)

