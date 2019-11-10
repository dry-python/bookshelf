from attr import attrib
from attr import attrs
from stories import arguments
from stories import Failure
from stories import Result
from stories import story
from stories import Success


@attrs
class ShowCategory:
    """Show category entries."""

    @story
    @arguments("category_id", "user")
    def show(I):

        I.find_category
        I.find_subscription
        I.check_expiration
        I.find_entries
        I.show_entries

    # Steps.

    def find_category(self, ctx):

        category = self.load_category(ctx.category_id)
        return Success(category=category)

    def find_subscription(self, ctx):

        subscription = self.load_subscription(ctx.user, ctx.category)
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

        entries = self.load_entries(ctx.category)
        return Success(entries=entries)

    def show_entries(self, ctx):

        return Result({"category": ctx.category, "entries": ctx.entries})

    # Dependencies.

    load_category = attrib()
    load_subscription = attrib()
    load_entries = attrib()
