from typing import Callable

from attr import attrs
from pydantic import BaseModel
from stories import arguments
from stories import Failure
from stories import Result
from stories import story
from stories import Success

from bookshelf.entities import Category
from bookshelf.entities import CategoryId
from bookshelf.entities import Notification
from bookshelf.entities import NotificationKind
from bookshelf.entities import Price
from bookshelf.entities import PriceId
from bookshelf.entities import Profile
from bookshelf.entities import ProfileId
from bookshelf.entities import Subscription


@attrs(auto_attribs=True)
class BuySubscription:
    """Buy subscription for certain category."""

    # TODO: Ignore repeated subscriptions.

    @story
    @arguments("category_id", "price_id", "profile_id")
    def buy(I):

        I.find_category
        I.find_price
        I.find_profile
        I.check_balance
        # TODO: Create payment record here.
        I.persist_payment
        I.persist_subscription
        I.prepare_subscription_notification
        I.send_notifications
        I.show_category

    # Steps.

    def find_category(self, ctx):

        category = self.load_category(ctx.category_id)
        return Success(category=category)

    def find_price(self, ctx):

        price = self.load_price(ctx.price_id)
        return Success(price=price)

    def find_profile(self, ctx):

        profile = self.load_profile(ctx.profile_id)
        return Success(profile=profile)

    def check_balance(self, ctx):

        if ctx.profile.can_afford(ctx.price):
            return Success()
        else:
            return Failure()

    def persist_payment(self, ctx):

        self.decrease_balance(ctx.profile, ctx.price.cost)
        return Success()

    def persist_subscription(self, ctx):

        expires = ctx.price.subscription_will_expire(self.current_date())
        subscription = self.create_subscription(ctx.profile, ctx.category, expires)
        return Success(subscription=subscription)

    def prepare_subscription_notification(self, ctx):

        notification = Notification(
            profile=ctx.profile, kind=NotificationKind.subscription
        )
        return Success(notifications=[notification])

    def show_category(self, ctx):

        return Result(ctx.category)

    # Dependencies.

    load_category: Callable
    load_price: Callable
    load_profile: Callable
    decrease_balance: Callable
    current_date: Callable
    create_subscription: Callable
    send_notifications: story


@BuySubscription.buy.contract
class Context(BaseModel):

    # Arguments.

    category_id: CategoryId
    price_id: PriceId
    profile_id: ProfileId

    # State.

    category: Category
    price: Price
    profile: Profile
    subscription: Subscription


# FIXME: Define failure protocol.
