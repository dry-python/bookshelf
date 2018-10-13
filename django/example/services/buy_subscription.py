from attr import attrib, attrs
from stories import Failure, Result, Success, argument, story


@attrs
class BuySubscription:
    """Buy subscription for certain category."""

    # TODO: Ignore repeated subscriptions.

    impl = attrib()

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

    def find_category(self):

        category = self.impl.load_category(self.ctx.category_id)
        return Success(category=category)

    def find_price(self):

        price = self.impl.load_price(self.ctx.price_id)
        return Success(price=price)

    def find_profile(self):

        profile = self.impl.load_profile(self.ctx.user)
        return Success(profile=profile)

    def check_balance(self):

        if self.ctx.profile.balance > self.ctx.price.cost:
            return Success()
        else:
            return Failure()

    def persist_payment(self):

        self.impl.del_balance(self.ctx.profile, self.ctx.price.cost)
        self.impl.save_profile(self.ctx.profile)
        return Success()

    def persist_subscription(self):

        expires = self.impl.calculate_period(self.ctx.price.period)
        subscription = self.impl.create_subscription(
            self.ctx.profile, self.ctx.category, expires
        )
        return Success(subscription=subscription)

    def send_subscription_notification(self):

        notification = self.impl.send_notification(
            "subscription", self.ctx.profile, self.ctx.category.name
        )
        return Success(notification=notification)

    def show_category(self):

        return Result(self.ctx.category)
