from dependencies import Injector, Package, operation
from dependencies.contrib.django import view


implemented = Package("example.implemented")
functions = Package("example.functions")


@view
class ProfileView(Injector):

    template_name = "profile.html"

    show_profile = implemented.ShowProfile.show

    render = functions.Render.do

    @operation
    def get(show_profile, render, user):

        return render(show_profile(user=user))
