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
    def put(self):

        self.find_profile()
        self.increase_balance()
        self.send_income_notification()

    def find_profile(self):

        profile = self.impl.load_profile(self.ctx.user)
        return Success(profile=profile)

    def increase_balance(self):

        self.impl.add_balance(self.ctx.profile, self.ctx.amount)
        self.impl.save_profile(self.ctx.profile)
        return Success()

    def send_income_notification(self):

        notification = self.impl.send_notification(
            "income", self.ctx.profile, self.ctx.amount
        )
        return Success(notification=notification)
