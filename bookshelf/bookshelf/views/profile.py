from dependencies import Injector
from dependencies import Package
from dependencies import value
from dependencies.contrib.django import template_view


repositories = Package("bookshelf.repositories")


@template_view
class ProfileView(Injector):

    template_name = "profile.html"

    load_profile = repositories.load_profile

    @value
    def extra_context(load_profile, request):

        return {"profile": load_profile(request.profile_id)}
