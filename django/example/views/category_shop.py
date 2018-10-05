from dependencies import Package, operation
from dependencies.contrib.django import view

from .utils import TemplateMixin


services = Package("example.services")


@view
class CategoryShop(TemplateMixin):

    template_name = "category_shop.html"

    categories_for_purchase = services.CategoriesForPurchase.list

    @operation
    def get(categories_for_purchase, render, user):

        return render(categories_for_purchase(user))
