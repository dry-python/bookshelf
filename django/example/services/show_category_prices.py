from attr import attrib, attrs
from stories import Result, Success, argument, story


@attrs
class ShopCategoryPrices:
    """Show purchase variants for category."""

    @story
    @argument("category_id")
    @argument("error_in")
    def show(self):

        self.find_category()
        self.find_prices()
        self.make_forms()
        self.show_purchase_form()

    # Points.

    def find_category(self):

        category = self.load_category(self.ctx.category_id)
        return Success(category=category)

    def find_prices(self):

        prices = self.load_prices(self.ctx.category)
        return Success(prices=prices)

    def make_forms(self):

        forms = self.instantiate_forms(**self.ctx("prices", "error_in"))
        return Success(forms=forms)

    def show_purchase_form(self):

        return Result(self.ctx("category", "prices", "forms"))

    # Dependencies.

    load_category = attrib()
    load_prices = attrib()
    instantiate_forms = attrib()
