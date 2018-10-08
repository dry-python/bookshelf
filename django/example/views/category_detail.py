from dependencies import Package, operation, this
from dependencies.contrib.django import view

from .utils import TemplateMixin


services = Package("example.services")
repositories = Package("example.repositories")


@view
class CategoryDetailView(TemplateMixin):

    template_name = "category_detail.html"

    show_category = services.ShowCategory.show
    load_category = repositories.load_category
    load_entries = repositories.load_entries

    category_id = this.kwargs["id"]

    @operation
    def get(show_category, category_id, user, render):

        return render(show_category(category_id, user))
