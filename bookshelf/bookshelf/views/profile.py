from dependencies import Injector
from dependencies import operation
from dependencies import Package
from dependencies.contrib.django import view


implemented = Package("bookshelf.implemented")


@view
class ProfileView(Injector):

    template_name = "profile.html"

    show_profile = implemented.ShowProfile.show

    @operation
    def get(show_profile, render, request):

        return render(show_profile(profile_id=request.profile_id))
