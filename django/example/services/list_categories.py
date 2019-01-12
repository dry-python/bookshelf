from attr import attrib, attrs
from stories import Result, Success, argument, story


@attrs
class ListCategories:
    """List cotegories available to the user."""

    @story
    @argument("user")
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
