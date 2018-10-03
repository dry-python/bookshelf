from dependencies import Injector, Package, operation
from dependencies.contrib.django import form_view

from example.forms import SignUpForm


services = Package("example.services")


@form_view
class SignUp(Injector):

    template_name = "sign_up.html"
    form_class = SignUpForm
    success_url = ""
