from dependencies import Injector, Package, operation, this
from dependencies.contrib.django import view
from django.shortcuts import redirect

from bookshelf.forms import SubscribeForm


implemented = Package("bookshelf.implemented")
functions = Package("bookshelf.functions")


@view
class BuySubscriptionView(Injector):

    template_name = "subscribe.html"
    form_class = SubscribeForm

    show_prices = implemented.ShowPrices.show_prices
    buy_subscription = implemented.BuySubscription.buy_subscription

    category_id = this.kwargs["id"]

    render = functions.Render.do

    @operation
    def get(show_prices, category_id, render):

        return render(show_prices(category_id=category_id, error_in=None))

    @operation
    def post(
        buy_subscription, show_prices, render, category_id, user, form_class, request
    ):

        form = form_class(request.POST, request.FILES)
        form.is_valid()
        price_id = form.cleaned_data["price_id"]
        result = buy_subscription.run(category_id=category_id, price_id=price_id, user=user)
        if result.is_success:
            return redirect(result.value)
        elif result.failed_on("check_balance"):
            return render(show_prices(category_id=category_id, error_in=price_id))
