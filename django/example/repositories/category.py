from django.db.models import Exists, OuterRef
from django.utils.timezone import now

from example.models import Category, Price


def load_category(category_id):

    return Category.objects.get(pk=category_id)


def categories():

    return Category.objects.all()


def categories_with_subscriptions(user):

    return Category.objects.filter(
        subscriptions__profile__user=user, subscriptions__expires__gt=now()
    )


def exclude_categories_with_subscriptions(categories, user):

    return categories.exclude(
        subscriptions__profile__user=user, subscriptions__expires__gt=now()
    )


def filter_categories_with_prices(categories):

    prices = Price.objects.filter(category=OuterRef("pk"))
    return categories.annotate(has_price=Exists(prices)).filter(has_price=True)
