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

    def find_category(self, ctx):

        category = self.impl.load_category(ctx.category_id)
        return Success(category=category)

    def find_price(self, ctx):

        price = self.impl.load_price(ctx.price_id)
        return Success(price=price)

    def find_profile(self, ctx):

        profile = self.impl.load_profile(ctx.user)
        return Success(profile=profile)

    def check_balance(self, ctx):

        if ctx.profile.balance > ctx.price.cost:
            return Success()
        else:
            return Failure()

    def persist_payment(self, ctx):

        self.impl.del_balance(ctx.profile, ctx.price.cost)
        self.impl.save_profile(ctx.profile)
        return Success()

    def persist_subscription(self, ctx):

        expires = self.impl.calculate_period(ctx.price.period)
        subscription = self.impl.create_subscription(ctx.profile, ctx.category, expires)
        return Success(subscription=subscription)

    def send_subscription_notification(self, ctx):

        notification = self.impl.send_notification(
            "subscription", ctx.profile, ctx.category.name
        )
        return Success(notification=notification)

    def show_category(self, ctx):

        return Result(ctx.category)
