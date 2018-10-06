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
        self.increment_balance()

    # Points.

    def find_profile(self):

        profile = self.load_profile(self.ctx.user)
        return Success(profile=profile)

    def increment_balance(self):

        self.add_balance(self.ctx.profile, self.ctx.amount)
        self.save_profile(self.ctx.profile)
        return Success()

    # Dependencies.

    load_profile = attrib()
    add_balance = attrib()
    save_profile = attrib()
