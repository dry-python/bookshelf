from attr import attrib, attrs
from dependencies import Injector, this
from django import shortcuts


@attrs
class Render:

    template_name = attrib()

    request = attrib()

    def do(self, context=None):

        return shortcuts.render(self.request, self.template_name, context)


class TemplateMixin(Injector):
    """
    Base injector used to create view, which renders a template.
    """

    render = this.Render.do
    Render = Render
