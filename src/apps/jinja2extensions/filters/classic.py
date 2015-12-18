"""An additionals filters that simplify the process of creating Jinja2
templates in Django applications.

"""


def defaults(value, default_value=''):
    """The filter replaces the ``null`` value to the default value.

    Examples, usage::

        Hello {{ user.name|defaults('everybody') }}!

    resulr as ``Hello J. Smit!`` if the ``user.name`` has value - ``J. Smit``
    or ``Hello everybody!`` - if the ``user.name`` is ``Null``.

    """
    return value if value else default_value

