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

    def find_category(self):

        category = self.impl.load_category(self.ctx.category_id)
        return Success(category=category)

    def find_subscription(self):

        subscription = self.impl.load_subscription(self.ctx.user, self.ctx.category)
        if subscription:
            return Success(subscription=subscription)
        else:
            return Failure()

    def check_expiration(self):

        if self.ctx.subscription.is_expired():
            return Failure()
        else:
            return Success()

    def find_entries(self):

        entries = self.impl.load_entries(self.ctx.category)
        return Success(entries=entries)

    def show_entries(self):

        return Result(self.ctx("category", "entries"))
