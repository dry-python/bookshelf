from django.template import Library


register = Library()


# Builtins.


@register.filter
def index(value, arg):
    """Get item operation similar to the value[arg] in Python."""

    return value[arg]
