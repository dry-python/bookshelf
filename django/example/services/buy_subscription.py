from attr import attrib, attrs
from stories import Result, Success, argument, story


@attrs
class BuySubscription:
    """Buy subscription for certain category."""

    @story
    @argument("category_id")
    def buy(self):

        self.find_category()
        self.show_category()

    # Points.

    def find_category(self):

        category = self.load_category(self.ctx.category_id)
        return Success(category=category)

    def show_category(self):

        return Result(self.ctx.category)

    # Dependencies.

    load_category = attrib()
