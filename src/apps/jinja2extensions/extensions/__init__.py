"""Add additionals extensions in to Jinja2 templates for Django applications.

This modules presents various extensions to simplify the development process
templates, such as: call the built-in functions of python or comfort work with
localization, etc.

The modules can be mentally divided into two groups:

    clean
        The modules that do not require the installation of additional
        dependencies.
    dirty
        Modules that require the installation of additional dependencies
        outside developers, for example:

            - `django-solid-i18n-urls`_
            - `sorl-thumbnail`_
            - etc.

For this reason, different extensions are described in single modules - that
not to install additional third-party applications without need in it.

.. ......................................................................... ..
.. _`django-solid-i18n-urls`:
    https://github.com/st4lk/django-solid-i18n-urls
.. _`sorl-thumbnail`:
    https://github.com/mariocesar/sorl-thumbnail

"""

