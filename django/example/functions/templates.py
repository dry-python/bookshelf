from django import shortcuts


class Render:
    """Injectable shortcut."""

    def __init__(self, template_name, request):

        self.template_name = template_name
        self.request = request

    def __call__(self, context=None):

        return shortcuts.render(self.request, self.template_name, context)
