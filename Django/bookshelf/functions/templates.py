from attr import attrib
from attr import attrs
from django import shortcuts


@attrs
class Render:
    """Injectable shortcut."""

    template_name = attrib()
    request = attrib()

    def do(self, context=None):

        return shortcuts.render(self.request, self.template_name, context)
