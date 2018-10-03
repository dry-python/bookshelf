from dependencies import Package, operation
from dependencies.contrib.django import view

from .utils import TemplateMixin


services = Package("example.services")


@view
class SignUp(TemplateMixin):

    template_name = "sign_up.html"

    @operation
    def get(render):

        return render()
