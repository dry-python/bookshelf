from dependencies import Package, operation
from dependencies.contrib.django import view

from .utils import TemplateMixin


services = Package("example.services")
repositories = Package("example.repositories")


@view
class CategoryShopView(TemplateMixin):

    template_name = "category_shop.html"

    categories_for_purchase = services.CategoriesForPurchase.list
    load_categories = repositories.categories
    exclude_subscriptions = repositories.exclude_categories_with_subscriptions
    filter_prices = repositories.filter_categories_with_prices
    load_prices = repositories.cheapest_price_by_category

    @operation
    def get(categories_for_purchase, render, user):

        return render(categories_for_purchase(user))
