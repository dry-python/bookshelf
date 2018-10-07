from dependencies import Injector, Package, operation
from dependencies.contrib.django import form_view

from example.forms import SubscribeForm


@form_view
class BuySubscriptionView(Injector):

    template_name = "subscribe.html"
    form_class = SubscribeForm

    @operation
    def form_valid(buy_subscription, user):

        pass
