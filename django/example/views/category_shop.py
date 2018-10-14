from dependencies import Injector, Package, operation
from dependencies.contrib.django import view


services = Package("example.services")
repositories = Package("example.repositories")
functions = Package("example.functions")


@view
class CategoryShopView(Injector):

    template_name = "category_shop.html"

    categories_for_purchase = services.CategoriesForPurchase.list

    class impl(Injector):

        load_categories = repositories.load_categories
        exclude_subscriptions = repositories.category.exclude_subscribed
        filter_prices = repositories.category.keep_with_prices
        load_prices = repositories.cheapest_price_by_category

    render = functions.Render.do

    @operation
    def get(categories_for_purchase, render, user):

        return render(categories_for_purchase(user))
