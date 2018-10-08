from datetime import timedelta

from django.utils.timezone import now
from django.utils.translation import gettext as _

from example.forms import SubscribeForm
from example.functions.utils import apply


@apply(list)
def make_subscription_forms(prices, error_in):

    for price in prices.values():
        form = SubscribeForm(initial={"price_id": price.pk})
        if price.pk == error_in:
            form.cleaned_data = {}  # I have no idea...
            form.add_error(None, _("You don't have enough money"))
        yield form


def calculate_period(period):

    return timedelta(days=period) + now()
