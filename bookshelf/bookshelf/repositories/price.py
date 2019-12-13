from decimal import Decimal
from typing import Dict
from typing import List

from django.db.models import Min
from mappers import Mapper

from bookshelf import models
from bookshelf.entities import Category
from bookshelf.entities import CategoryId
from bookshelf.entities import Price
from bookshelf.entities import PriceId


mapper = Mapper(Price, models.Price, {"primary_key": "id"})


@mapper.reader
def load_price(price_id: PriceId) -> Price:
    return models.Price.objects.filter(pk=price_id)


# FIXME: This should be mappers too.


def prices_for_category(category: Category) -> Dict[PriceId, Price]:
    return {price.pk: price for price in Price.objects.filter(category=category)}


# FIXME: This should return Dict[CategoryId, Price].


def load_cheapest_prices_for_categories(
    categories: List[Category],
) -> Dict[CategoryId, Decimal]:
    return {
        price["category"]: price["min_cost"]
        for price in models.Price.objects.filter(
            category__in=[category.primary_key for category in categories]
        )
        .values("category")
        .annotate(min_cost=Min("cost"))
        .order_by()
    }
