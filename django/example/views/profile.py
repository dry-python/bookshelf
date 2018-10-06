from dependencies import Package, operation
from dependencies.contrib.django import view

from .utils import TemplateMixin


services = Package("example.services")


@view
class Profile(TemplateMixin):

    template_name = "profile.html"

    show_profile = services.ShowProfile.show

    @operation
    def get(show_profile, render, user):

        return render(show_profile(user))
