from datetime import timedelta

from django.utils.timezone import now

from example.forms import SubscribeForm


def make_subscription_forms(prices):

    return [SubscribeForm(initial={"price_id": price.pk}) for price in prices.values()]


def calculate_period(period):

    return timedelta(days=period) + now()
