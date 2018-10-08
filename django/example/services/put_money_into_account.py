from attr import attrib, attrs
from stories import Success, argument, story


@attrs
class PutMoneyIntoAccount:
    """Put money into user account."""

    # TODO: Use external payment gateway in the future.

    @story
    @argument("user")
    @argument("amount")
    def put(self):

        self.find_profile()
        self.increase_balance()
        self.send_income_notification()

    # Points.

    def find_profile(self):

        profile = self.load_profile(self.ctx.user)
        return Success(profile=profile)

    def increase_balance(self):

        self.add_balance(self.ctx.profile, self.ctx.amount)
        self.save_profile(self.ctx.profile)
        return Success()

    def send_income_notification(self):

        notification = self.send_notification(
            "income", self.ctx.profile, self.ctx.amount
        )
        return Success(notification=notification)

    # Dependencies.

    load_profile = attrib()
    add_balance = attrib()
    save_profile = attrib()
    send_notification = attrib()
