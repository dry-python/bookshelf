from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.views.generic import FormView

from bookshelf.forms import SubscribeForm
from bookshelf.implemented import BuySubscription


class BuySubscriptionView(FormView):
    template_name = "subscribe.html"
    form_class = SubscribeForm  # FIXME: Use form set here.

    def form_valid(self, form):
        result = BuySubscription.buy_subscription.run(
            category_id=self.kwargs["id"],
            price_id=form.cleaned_data["price_id"],
            profile_id=self.request.profile_id,
        )
        if result.is_success:
            return redirect(result.value)
        elif result.failed_on("check_balance"):
            form.add_error("...", _("..."))
            return self.form_invalid(form)
