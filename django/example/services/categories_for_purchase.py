from attr import attrib, attrs
from stories import Result, Success, argument, story


@attrs
class CategoriesForPurchase:
    """List categories available to user for purchase."""

    impl = attrib()

    @story
    @argument("user")
    def list(self):

        self.find_categories()
        self.keep_without_subscriptions()
        self.keep_with_prices()
        self.find_cheapest_prices()
        self.show_categories()

    def find_categories(self, ctx):

        categories = self.impl.load_categories()
        return Success(categories=categories)

    def keep_without_subscriptions(self, ctx):

        categories = self.impl.exclude_subscriptions(ctx.categories, ctx.user)
        return Success(no_subscriptions=categories)

    def keep_with_prices(self, ctx):

        categories = self.impl.filter_prices(ctx.no_subscriptions)
        return Success(with_prices=categories)

    def find_cheapest_prices(self, ctx):

        prices = self.impl.load_prices(ctx.with_prices)
        return Success(prices=prices)

    def show_categories(self, ctx):

        return Result(ctx("prices", categories="with_prices"))
