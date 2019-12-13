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


@mapper.reader
def load_categories_for_purchase(profile_id: ProfileId) -> List[Category]:
    prices = models.Price.objects.filter(category=OuterRef("pk"))
    return (
        models.Category.objects.exclude(
            subscription__profile_id=profile_id, subscription__expires__gt=now()
        )
        .annotate(has_price=Exists(prices))
        .filter(has_price=True)
    )
