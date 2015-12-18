from jinja2.ext import Extension


class BuiltInFunctionsExtension(Extension):
    """The Jinja2 special tags that call some the built-in functions of python.

    EXTENSIONS

        abs
            To call the ``abs()`` method of python (`abs detail`_).
        all
            To call the ``all()`` method of python (`all detail`_).
        any
            To call the ``any()`` method of python (`any detail`_).
        dir
            To call the ``dir()`` method of python (`dir detail`_).
        type
            To call the ``type()`` method of python (`type detail`_).

    .. ..................................................................... ..
    .. _`abs detail`:
        https://docs.python.org/3/library/functions.html#abs
    .. _`all detail`:
        https://docs.python.org/3/library/functions.html#all
    .. _`any detail`:
        https://docs.python.org/3/library/functions.html#any
    .. _`dir detail`:
        https://docs.python.org/3/library/functions.html#dir
    .. _`type detail`:
        https://docs.python.org/3/library/functions.html#type

    """
    def __init__(self, environment):
        """Initialize globals."""
        environment.globals['abs'] = self._abs
        environment.globals['all'] = self._all
        environment.globals['dir'] = self._dir
        environment.globals['type'] = self._type
        environment.globals['str'] = self._str

    def _abs(self, object):
        return abs(object)

    def _all(self, object):
        return all(object)

    def _any(self, object):
        return any(object)

    def _dir(self, object):
        return dir(object)

    def _type(self, object):
        return type(object)

    def _str(self, object):
        return 'en'

