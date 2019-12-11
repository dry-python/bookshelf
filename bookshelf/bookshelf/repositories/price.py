from decimal import Decimal
from typing import Dict
from typing import List

from django.db import connection
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


def load_cheapest_prices_for_categories(
    categories: List[Category],
) -> Dict[CategoryId, Decimal]:
    query = """
    SELECT "category_id",
           MIN("cost")
      FROM "bookshelf_price"
     WHERE "id" IN (
       SELECT "id"
         FROM "bookshelf_price"
        WHERE "category_id" IN %s
        GROUP BY "category_id", "period"
       HAVING "from_date" = MAX("from_date")
     )
     GROUP BY "category_id"
    """
    argument = [category.primary_key for category in categories]
    with connection.cursor() as cursor:
        cursor.execute(query, [argument])
        return {k: v for k, v in cursor.fetchall()}
