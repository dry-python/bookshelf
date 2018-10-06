from django.db.models import Min

from example.models import Price


def cheapest_price_by_category(categories):

    # FIXME: Filter by most recent date for each category and period.
    return {
        each["category"]: each["min_cost"]
        for each in Price.objects.filter(pk__in=categories)
        .values("category")
        .annotate(min_cost=Min("cost"))
        .order_by()
    }
