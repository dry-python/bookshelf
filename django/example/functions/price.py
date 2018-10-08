from example.forms import SubscribeForm


def make_subscription_forms(prices):

    return [SubscribeForm(initial={"price_id": price.pk}) for price in prices.values()]
