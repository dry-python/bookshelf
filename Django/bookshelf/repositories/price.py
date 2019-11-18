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


def prices_for_category(category: Category) -> Dict[PriceId, Price]:
    return {price.pk: price for price in Price.objects.filter(category=category)}


def cheapest_price_by_category(categories: List[Category]) -> Dict[CategoryId, int]:

    # FIXME: Express this query.
    #
    # SELECT "category_id",
    #        MIN("cost")
    #   FROM "bookshelf_price"
    #  WHERE "id" IN (
    #    SELECT "id"
    #      FROM "bookshelf_price"
    #     WHERE "category_id" IN (1, 2, 3, 4)
    #     GROUP BY "category_id", "period"
    #    HAVING "from_date" = MAX("from_date")
    #  )
    #  GROUP BY "category_id"

    return {
        each["category"]: each["min_cost"]
        for each in Price.objects.filter(category__in=categories)
        .values("category")
        .annotate(min_cost=Min("cost"))
        .order_by()
    }
