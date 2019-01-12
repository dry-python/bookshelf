from attr import attrib, attrs
from stories import Result, Success, argument, story


@attrs
class CategoriesForPurchase:
    """List categories available to user for purchase."""

    @story
    @argument("user")
    def list(I):

        I.find_categories
        I.keep_without_subscriptions
        I.keep_with_prices
        I.find_cheapest_prices
        I.show_categories

    # Steps.

    def find_categories(self, ctx):

        categories = self.load_categories()
        return Success(categories=categories)

    def keep_without_subscriptions(self, ctx):

        categories = self.exclude_subscriptions(ctx.categories, ctx.user)
        return Success(no_subscriptions=categories)

    def keep_with_prices(self, ctx):

        categories = self.filter_prices(ctx.no_subscriptions)
        return Success(with_prices=categories)

    def find_cheapest_prices(self, ctx):

        prices = self.load_prices(ctx.with_prices)
        return Success(prices=prices)

    def show_categories(self, ctx):

        return Result(ctx("prices", categories="with_prices"))

    # Dependencies.

    load_categories = attrib()
    exclude_subscriptions = attrib()
    filter_prices = attrib()
    load_prices = attrib()
