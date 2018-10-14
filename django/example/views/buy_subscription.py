from dependencies import Injector, Package, operation, this
from dependencies.contrib.django import view
from django.shortcuts import redirect

from example.forms import SubscribeForm


services = Package("example.services")
repositories = Package("example.repositories")
functions = Package("example.functions")


@view
class BuySubscriptionView(Injector):

    template_name = "subscribe.html"
    form_class = SubscribeForm

    show_prices = this.ShowPrices.show_prices

    class ShowPrices(Injector):

        show_prices = services.ShopCategoryPrices.show

        class impl(Injector):

            load_category = repositories.load_category
            load_prices = repositories.prices_for_category
            instantiate_forms = functions.make_subscription_forms

    render = functions.Render.do

    category_id = this.kwargs["id"]

    @operation
    def get(show_prices, category_id, render):

        return render(show_prices(category_id, None))

    buy_subscription = this.BuySubscription.buy_subscription

    class BuySubscription(Injector):

        buy_subscription = services.BuySubscription.buy

        class impl(Injector):

            load_category = repositories.load_category
            load_price = repositories.load_price
            load_profile = repositories.load_profile
            del_balance = repositories.del_balance
            save_profile = repositories.save_profile
            calculate_period = functions.calculate_period
            create_subscription = repositories.create_subscription
            send_notification = functions.SendNotification.do
            messages = functions.Messages
            create_notification = repositories.create_notification

    @operation
    def post(
        buy_subscription, show_prices, render, category_id, user, form_class, request
    ):

        form = form_class(request.POST, request.FILES)
        form.is_valid()
        price_id = form.cleaned_data["price_id"]
        result = buy_subscription.run(category_id, price_id, user)
        if result.is_success:
            return redirect(result.value)
        elif result.failed_on("check_balance"):
            return render(show_prices(category_id, price_id))
