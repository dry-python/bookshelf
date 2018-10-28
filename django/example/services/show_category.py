from attr import attrib, attrs
from stories import Failure, Result, Success, argument, story


@attrs
class ShowCategory:
    """Show category entries."""

    impl = attrib()

    @story
    @argument("category_id")
    @argument("user")
    def show(self):

        self.find_category()
        self.find_subscription()
        self.check_expiration()
        self.find_entries()
        self.show_entries()

    def find_category(self, ctx):

        category = self.impl.load_category(ctx.category_id)
        return Success(category=category)

    def find_subscription(self, ctx):

        subscription = self.impl.load_subscription(ctx.user, ctx.category)
        if subscription:
            return Success(subscription=subscription)
        else:
            return Failure()

    def check_expiration(self, ctx):

        if ctx.subscription.is_expired():
            return Failure()
        else:
            return Success()

    def find_entries(self, ctx):

        entries = self.impl.load_entries(ctx.category)
        return Success(entries=entries)

    def show_entries(self, ctx):

        return Result(ctx("category", "entries"))
