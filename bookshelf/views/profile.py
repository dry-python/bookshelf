from django.views.generic import TemplateView

from bookshelf.repositories import load_profile


class ProfileView(TemplateView):
    template_name = "profile.html"

    @property
    def extra_context(self):
        return {"profile": load_profile(self.request.profile_id)}
