from django.db.models import Min

from example.models import Price


def load_price(price_id):

    return Price.objects.get(pk=price_id)


def prices_for_category(category):

    return {price.pk: price for price in Price.objects.filter(category=category)}


def cheapest_price_by_category(categories):

    # FIXME: Filter by most recent date for each category and period.
    return {
        each["category"]: each["min_cost"]
        for each in Price.objects.filter(pk__in=categories)
        .values("category")
        .annotate(min_cost=Min("cost"))
        .order_by()
    }
