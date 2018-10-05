from dependencies import Package, operation
from dependencies.contrib.django import view

from .utils import TemplateMixin


services = Package("example.services")
repositories = Package("example.repositories")


@view
class CategoryShop(TemplateMixin):

    template_name = "category_shop.html"

    categories_for_purchase = services.CategoriesForPurchase.list
    load_categories = repositories.categories_without_subscriptions

    @operation
    def get(categories_for_purchase, render, user):

        return render(categories_for_purchase(user))
