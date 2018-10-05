from attr import attrib, attrs
from stories import Result, Success, argument, story


@attrs
class CategoriesForPurchase:
    """List categories available to user for purchase."""

    @story
    @argument("user")
    def list(self):

        self.find_categories_without_subscriptions()
        self.show_categories()

    # Points.

    def find_categories_without_subscriptions(self):

        categories = self.load_categories(self.ctx.user)
        return Success(categories=categories)

    def show_categories(self):

        return Result(dict(**self.ctx("categories")))

    # Dependencies.

    load_categories = attrib()
