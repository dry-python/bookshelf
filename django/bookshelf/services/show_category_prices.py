from attr import attrib, attrs
from stories import Result, Success, arguments, story


@attrs
class ShopCategoryPrices:
    """Show purchase variants for category."""

    @story
    @arguments("category_id", "error_in")
    def show(I):

        I.find_category
        I.find_prices
        I.make_forms
        I.show_purchase_form

    # Steps.

    def find_category(self, ctx):

        category = self.load_category(ctx.category_id)
        return Success(category=category)

    def find_prices(self, ctx):

        prices = self.load_prices(ctx.category)
        return Success(prices=prices)

    def make_forms(self, ctx):

        forms = self.instantiate_forms(prices=ctx.prices, error_in=ctx.error_in)
        return Success(forms=forms)

    def show_purchase_form(self, ctx):

        return Result({
            "category": ctx.category,
            "prices": ctx.prices,
            "forms": ctx.forms,
        })

    # Dependencies.

    load_category = attrib()
    load_prices = attrib()
    instantiate_forms = attrib()
