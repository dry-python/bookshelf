from typing import List

from django.db.models import Exists
from django.db.models import OuterRef
from django.utils.timezone import now
from mappers import Mapper

from bookshelf import models
from bookshelf.entities import Category
from bookshelf.entities import CategoryId
from bookshelf.entities import ProfileId

mapper = Mapper(Category, models.Category, {"primary_key": "id"})


@mapper.reader
def load_category(category_id: CategoryId) -> Category:
    return models.Category.objects.filter(pk=category_id)


@mapper.reader
def load_subscribed_categories(profile_id: ProfileId) -> List[Category]:
    return models.Category.objects.filter(
        subscription__profile_id=profile_id, subscription__expires__gt=now()
    )


def exclude_subscribed(categories, user):
    return categories.exclude(
        subscriptions__profile__user=user, subscriptions__expires__gt=now()
    )


def keep_with_prices(categories):
    prices = models.Price.objects.filter(category=OuterRef("pk"))
    return categories.annotate(has_price=Exists(prices)).filter(has_price=True)
