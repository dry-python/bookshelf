from dependencies import Injector, Package, operation
from dependencies.contrib.django import view


services = Package("example.services")
repositories = Package("example.repositories")
functions = Package("example.functions")


@view
class ProfileView(Injector):

    template_name = "profile.html"

    show_profile = services.ShowProfile.show

    class impl(Injector):

        load_profile = repositories.load_profile

    render = functions.Render.do

    @operation
    def get(show_profile, render, user):

        return render(show_profile(user))
