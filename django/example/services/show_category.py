from attr import attrib, attrs
from stories import Result, Success, argument, story


@attrs
class ShowCategory:
    """Show category entries."""

    @story
    @argument("category_id")
    @argument("user")
    def show(self):

        self.find_category()
        self.check_subscription()
        self.find_entries()
        self.show_entries()

    # Points.

    def find_category(self):

        category = self.load_category(self.ctx.category_id)
        return Success(category=category)

    def check_subscription(self):

        return Success()

    def find_entries(self):

        entries = self.load_entries(self.ctx.category)
        return Success(entries=entries)

    def show_entries(self):

        return Result(self.ctx("entries"))

    # Dependencies.

    load_category = attrib()
    load_entries = attrib()
