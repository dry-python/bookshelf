from dependencies import Injector
from dependencies import operation
from dependencies import Package
from dependencies.contrib.django import view


implemented = Package("bookshelf.implemented")
functions = Package("bookshelf.functions")


@view
class ProfileView(Injector):

    template_name = "profile.html"

    show_profile = implemented.ShowProfile.show

    render = functions.Render.do

    @operation
    def get(show_profile, render, request):

        return render(show_profile(profile_id=request.profile_id))
