from dependencies import Injector
from dependencies import Package
from dependencies import value
from dependencies.contrib.django import template_view


repositories = Package("bookshelf.repositories")


@template_view
class CategoryListView(Injector):

    template_name = "category_list.html"

    load_categories = repositories.load_subscribed_categories

    @value
    def extra_context(load_categories, request):

        return {"categories": load_categories(request.profile_id)}
