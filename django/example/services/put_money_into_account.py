from attr import attrib, attrs
from stories import Success, arguments, story


@attrs
class PutMoneyIntoAccount:
    """Put money into user account."""

    # TODO: Use external payment gateway in the future.

    @story
    @arguments("user", "amount")
    def put(I):

        I.find_profile
        I.increase_balance
        I.send_income_notification

    # Steps.

    def find_profile(self, ctx):

        profile = self.load_profile(ctx.user)
        return Success(profile=profile)

    def increase_balance(self, ctx):

        self.add_balance(ctx.profile, ctx.amount)
        self.save_profile(ctx.profile)
        return Success()

    def send_income_notification(self, ctx):

        notification = self.send_notification("income", ctx.profile, ctx.amount)
        return Success(notification=notification)

    # Dependencies.

    load_profile = attrib()
    add_balance = attrib()
    save_profile = attrib()
    send_notification = attrib()
    messages = attrib()
    create_notification = attrib()
