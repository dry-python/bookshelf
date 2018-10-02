from dependencies import Injector, operation
from django import shortcuts


class TemplateMixin(Injector):
    """
    Base injector used to create view, which renders a template.
    """

    @operation
    def render(template_name, request):

        return shortcuts.render(request, template_name)
