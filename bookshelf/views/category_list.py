from django.views.generic import TemplateView

from bookshelf.repositories import load_subscribed_categories


class CategoryListView(TemplateView):
    template_name = "category_list.html"

    @property
    def extra_context(self):
        return {"categories": load_subscribed_categories(self.request.profile_id)}
