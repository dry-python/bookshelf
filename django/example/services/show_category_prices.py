from attr import attrib, attrs
from stories import Result, Success, argument, story


@attrs
class ShopCategoryPrices:
    """Show purchase variants for category."""

    impl = attrib()

    @story
    @argument("category_id")
    @argument("error_in")
    def show(self):

        self.find_category()
        self.find_prices()
        self.make_forms()
        self.show_purchase_form()

    def find_category(self, ctx):

        category = self.impl.load_category(ctx.category_id)
        return Success(category=category)

    def find_prices(self, ctx):

        prices = self.impl.load_prices(ctx.category)
        return Success(prices=prices)

    def make_forms(self, ctx):

        forms = self.impl.instantiate_forms(**ctx("prices", "error_in"))
        return Success(forms=forms)

    def show_purchase_form(self, ctx):

        return Result(ctx("category", "prices", "forms"))
