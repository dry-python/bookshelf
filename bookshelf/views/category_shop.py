from django.views.generic import TemplateView

from bookshelf.repositories import load_categories_for_purchase
from bookshelf.repositories import load_cheapest_prices_for_categories


class CategoryShopView(TemplateView):
    template_name = "category_shop.html"

    @property
    def extra_context(self):
        categories = load_categories_for_purchase(self.request.profile_id)
        prices = load_cheapest_prices_for_categories(categories)
        return {"categories": categories, "prices": prices}
