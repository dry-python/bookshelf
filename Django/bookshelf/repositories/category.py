from django.db.models import Exists
from django.db.models import OuterRef
from django.utils.timezone import now

from bookshelf.models import Category
from bookshelf.models import Price


def load_category(category_id):

    return Category.objects.get(pk=category_id)


def load_categories():

    return Category.objects.all()


def keep_subscribed(categories, user):

    return categories.filter(
        subscriptions__profile__user=user, subscriptions__expires__gt=now()
    )


def exclude_subscribed(categories, user):

    return categories.exclude(
        subscriptions__profile__user=user, subscriptions__expires__gt=now()
    )


def keep_with_prices(categories):

    prices = Price.objects.filter(category=OuterRef("pk"))
    return categories.annotate(has_price=Exists(prices)).filter(has_price=True)
