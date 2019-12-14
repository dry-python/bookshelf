from dependencies import Injector
from dependencies import operation
from dependencies import Package
from dependencies import this
from dependencies.contrib.django import form_view
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _

from bookshelf.forms import SubscribeForm


implemented = Package("bookshelf.implemented")


@form_view
class BuySubscriptionView(Injector):

    template_name = "subscribe.html"
    form_class = SubscribeForm  # FIXME: Use form set here.

    buy_subscription = implemented.BuySubscription.buy_subscription

    category_id = this.kwargs["id"]
    price_id = this.form.cleaned_data["price_id"]

    @operation
    def form_valid(buy_subscription, category_id, price_id, form, view, request):

        result = buy_subscription.run(
            category_id=category_id, price_id=price_id, profile_id=request.profile_id
        )
        if result.is_success:
            return redirect(result.value)
        elif result.failed_on("check_balance"):
            form.add_error("...", _("..."))
            return view.form_invalid(form)
