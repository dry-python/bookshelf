from attr import attrib, attrs
from stories import Result, Success, argument, story


@attrs
class ListCategories:
    """List cotegories available to the user."""

    impl = attrib()

    @story
    @argument("user")
    def list(self):

        self.find_categories()
        self.keep_with_subscriptions()
        self.show_categories()

    def find_categories(self):

        categories = self.impl.load_categories()
        return Success(categories=categories)

    def keep_with_subscriptions(self):

        categories = self.impl.keep_subscriptions(self.ctx.categories, self.ctx.user)
        return Success(subscribed=categories)

    def show_categories(self):

        return Result({"categories": self.ctx.subscribed})
