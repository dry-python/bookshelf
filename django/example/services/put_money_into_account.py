from attr import attrib, attrs
from stories import Success, argument, story


@attrs
class PutMoneyIntoAccount:
    """Put money into user account."""

    # TODO: Use external payment gateway in the future.

    impl = attrib()

    @story
    @argument("user")
    @argument("amount")
    def put(I):

        I.find_profile
        I.increase_balance
        I.send_income_notification

    def find_profile(self, ctx):

        profile = self.impl.load_profile(ctx.user)
        return Success(profile=profile)

    def increase_balance(self, ctx):

        self.impl.add_balance(ctx.profile, ctx.amount)
        self.impl.save_profile(ctx.profile)
        return Success()

    def send_income_notification(self, ctx):

        notification = self.impl.send_notification("income", ctx.profile, ctx.amount)
        return Success(notification=notification)
