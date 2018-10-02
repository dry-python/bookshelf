from dependencies import Package, operation
from dependencies.contrib.django import view

from .utils import TemplateMixin


services = Package("example.services")


@view
class CategoryList(TemplateMixin):

    template_name = "category_list.html"

    list_categories = services.ListCategories.list

    @operation
    def get(list_categories, render, user):
        result = list_categories.run(user)
        if result.is_success:
            return render(result.value)
