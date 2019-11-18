from attr import attrib
from attr import attrs
from stories import arguments
from stories import Failure
from stories import Result
from stories import story
from stories import Success


@attrs
class BuySubscription:
    """Buy subscription for certain category."""

    # TODO: Ignore repeated subscriptions.

    @story
    @arguments("category_id", "price_id", "user")
    def buy(I):

        I.find_category
        I.find_price
        I.find_profile
        I.check_balance
        I.persist_payment
        I.persist_subscription
        I.send_subscription_notification
        I.show_category

    # Steps.

    def find_category(self, ctx):

        category = self.load_category(ctx.category_id)
        return Success(category=category)

    def find_price(self, ctx):

        price = self.load_price(ctx.price_id)
        return Success(price=price)

    def find_profile(self, ctx):

        profile = self.load_profile(ctx.user)
        return Success(profile=profile)

    def check_balance(self, ctx):

        if ctx.profile.balance > ctx.price.cost:
            return Success()
        else:
            return Failure()

    def persist_payment(self, ctx):

        self.decrease_balance(ctx.profile, ctx.price.cost)
        self.save_profile(ctx.profile)
        return Success()

    def persist_subscription(self, ctx):

        expires = self.calculate_period(ctx.price.period)
        subscription = self.create_subscription(ctx.profile, ctx.category, expires)
        return Success(subscription=subscription)

    def send_subscription_notification(self, ctx):

        notification = self.send_notification(
            "subscription", ctx.profile, ctx.category.name
        )
        return Success(notification=notification)

    def show_category(self, ctx):

        return Result(ctx.category)

    # Dependencies.

    load_category = attrib()
    load_price = attrib()
    load_profile = attrib()
    decrease_balance = attrib()
    save_profile = attrib()
    calculate_period = attrib()
    create_subscription = attrib()
    send_notification = attrib()
    messages = attrib()
    create_notification = attrib()
