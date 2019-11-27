from attr import attrs
from django import shortcuts
from django.http import HttpRequest


@attrs(auto_attribs=True)
class Render:
    """Injectable shortcut."""

    template_name: str
    request: HttpRequest

    def do(self, context=None):

        return shortcuts.render(self.request, self.template_name, context)
