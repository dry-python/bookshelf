from dependencies import Package, operation
from dependencies.contrib.django import view

from .utils import TemplateMixin


services = Package("example.services")
repositories = Package("example.repositories")


@view
class CategoryListView(TemplateMixin):

    template_name = "category_list.html"

    list_categories = services.ListCategories.list
    load_categories = repositories.load_categories
    keep_subscriptions = repositories.category.keep_subscribed

    @operation
    def get(list_categories, render, user):

        return render(list_categories(user))
