from typing import List

from django.db.models import Exists
from django.db.models import OuterRef
from django.utils.timezone import now
from mappers import Mapper

from bookshelf import models
from bookshelf.entities import Category
from bookshelf.entities import CategoryId

mapper = Mapper(Category, models.Category, {"primary_key": "id"})


@mapper.reader
def load_category(category_id: CategoryId) -> Category:
    return models.Category.objects.filter(pk=category_id)


@mapper.reader
def load_categories() -> List[Category]:
    return models.Category.objects.all()


def keep_subscribed(categories, user):
    return categories.filter(
        subscriptions__profile__user=user, subscriptions__expires__gt=now()
    )


def exclude_subscribed(categories, user):
    return categories.exclude(
        subscriptions__profile__user=user, subscriptions__expires__gt=now()
    )


def keep_with_prices(categories):
    prices = models.Price.objects.filter(category=OuterRef("pk"))
    return categories.annotate(has_price=Exists(prices)).filter(has_price=True)
