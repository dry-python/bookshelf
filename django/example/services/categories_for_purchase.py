from attr import attrib, attrs
from stories import Result, Success, argument, story


@attrs
class CategoriesForPurchase:
    """List categories available to user for purchase."""

    @story
    @argument("user")
    def list(self):

        self.find_categories()
        self.keep_without_subscriptions()
        self.keep_with_prices()
        self.find_cheapest_prices()
        self.show_categories()

    # Points.

    def find_categories(self):

        categories = self.load_categories()
        return Success(categories=categories)

    def keep_without_subscriptions(self):

        categories = self.exclude_subscriptions(self.ctx.categories, self.ctx.user)
        return Success(no_subscriptions=categories)

    def keep_with_prices(self):

        categories = self.filter_prices(self.ctx.no_subscriptions)
        return Success(with_prices=categories)

    def find_cheapest_prices(self):

        prices = self.load_prices(self.ctx.with_prices)
        return Success(prices=prices)

    def show_categories(self):

        return Result(self.ctx("prices", categories="with_prices"))

    # Dependencies.

    load_categories = attrib()
    exclude_subscriptions = attrib()
    filter_prices = attrib()
    load_prices = attrib()
