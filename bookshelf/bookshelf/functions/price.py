from django.utils.translation import gettext as _

from bookshelf.forms import SubscribeForm
from bookshelf.functions.utils import apply


@apply(list)
def make_subscription_forms(prices, error_in):

    for price in prices.values():
        form = SubscribeForm(initial={"price_id": price.pk})
        if price.pk == error_in:
            form.cleaned_data = {}  # I have no idea...
            form.add_error(None, _("You don't have enough money"))
        yield form
