from attr import attrib, attrs
from stories import Result, Success, argument, story


@attrs
class ListCategories:
    """List cotegories available to the user."""

    @story
    @argument("user")
    def list(self):

        self.find_categories_with_subscriptions()
        self.show_categories()

    # Points.

    def find_categories_with_subscriptions(self):

        categories = self.load_categories(self.ctx.user)
        return Success(categories=categories)

    def show_categories(self):

        return Result(dict(**self.ctx("categories")))

    # Dependencies.

    load_categories = attrib()
