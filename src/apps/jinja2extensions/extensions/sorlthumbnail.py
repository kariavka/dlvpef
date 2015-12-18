from jinja2.ext import Extension
from sorl.thumbnail.shortcuts import get_thumbnail


class SorlThumbnailExtension(Extension):
    """..."""

    def __init__(self, environment):
        """Initialize globals."""
        environment.globals['thumbnail'] = self._thumbnail

    def _thumbnail(self, image, geometry_string, **options):
        try:
            thumbnail = get_thumbnail(image, geometry_string, **options)
        except IOError:
            thumbnail = None

        return thumbnail

