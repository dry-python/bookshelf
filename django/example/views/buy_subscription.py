from dependencies import Package, operation, this
from dependencies.contrib.django import view

from .utils import TemplateMixin


services = Package("example.services")
repositories = Package("example.repositories")
functions = Package("example.functions")


@view
class BuySubscriptionView(TemplateMixin):

    template_name = "subscribe.html"

    show_prices = services.ShopCategoryPrices.show
    load_category = repositories.load_category
    load_prices = repositories.prices_for_category
    instantiate_forms = functions.make_subscription_forms

    category_id = this.kwargs["id"]

    @operation
    def get(show_prices, category_id, render):

        return render(show_prices(category_id))

    @operation
    def post(buy_subscription, user):

        pass
