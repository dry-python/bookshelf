from attr import attrib
from attr import attrs
from stories import arguments
from stories import Result
from stories import story
from stories import Success


@attrs
class ListCategories:
    """List cotegories available to the user."""

    @story
    @arguments("user")
    def list(I):

        I.find_categories
        I.keep_with_subscriptions
        I.show_categories

    # Steps.

    def find_categories(self, ctx):

        categories = self.load_categories()
        return Success(categories=categories)

    def keep_with_subscriptions(self, ctx):

        categories = self.keep_subscriptions(ctx.categories, ctx.user)
        return Success(subscribed=categories)

    def show_categories(self, ctx):

        return Result({"categories": ctx.subscribed})

    # Dependencies.

    load_categories = attrib()
    keep_subscriptions = attrib()
