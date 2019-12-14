from dependencies import Injector
from dependencies import Package
from dependencies import value
from dependencies.contrib.django import template_view


repositories = Package("bookshelf.repositories")


@template_view
class CategoryShopView(Injector):

    template_name = "category_shop.html"

    load_categories = repositories.load_categories_for_purchase

    load_prices = repositories.load_cheapest_prices_for_categories

    @value
    def extra_context(load_categories, load_prices, request):

        categories = load_categories(request.profile_id)
        prices = load_prices(categories)
        return {"categories": categories, "prices": prices}
