from attr import attrib, attrs
from stories import Failure, Result, Success, argument, story


@attrs
class BuySubscription:
    """Buy subscription for certain category."""

    @story
    @argument("category_id")
    @argument("price_id")
    @argument("user")
    def buy(self):

        self.find_category()
        self.find_price()
        self.find_profile()
        self.check_balance()
        self.persist_payment()
        self.persist_subscription()
        self.send_subscription_notification()
        self.show_category()

    # Points.

    def find_category(self):

        category = self.load_category(self.ctx.category_id)
        return Success(category=category)

    def find_price(self):

        price = self.load_price(self.ctx.price_id)
        return Success(price=price)

    def find_profile(self):

        profile = self.load_profile(self.ctx.user)
        return Success(profile=profile)

    def check_balance(self):

        if self.ctx.profile.balance > self.ctx.price.cost:
            return Success()
        else:
            return Failure()

    def persist_payment(self):

        self.del_balance(self.ctx.profile, self.ctx.price.cost)
        self.save_profile(self.ctx.profile)
        return Success()

    def persist_subscription(self):

        expires = self.calculate_period(self.ctx.price.period)
        subscription = self.create_subscription(
            self.ctx.profile, self.ctx.category, expires
        )
        return Success(subscription=subscription)

    def send_subscription_notification(self):

        notification = self.send_notification(self.ctx.profile, "subscription")
        return Success(notification=notification)

    def show_category(self):

        return Result(self.ctx.category)

    # Dependencies.

    load_category = attrib()
    load_price = attrib()
    load_profile = attrib()
    del_balance = attrib()
    save_profile = attrib()
    calculate_period = attrib()
    create_subscription = attrib()
    send_notification = attrib()
