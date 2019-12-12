from decimal import Decimal
from typing import Callable

from attr import attrs
from pydantic import BaseModel
from stories import arguments
from stories import story
from stories import Success

from bookshelf.entities import Notification
from bookshelf.entities import Profile
from bookshelf.entities import ProfileId


@attrs(auto_attribs=True)
class PutMoneyIntoAccount:
    """Put money into user account."""

    # TODO: Use external payment gateway in the future.

    @story
    @arguments("profile_id", "amount")
    def put(I):

        I.find_profile
        I.increase_balance
        # TODO: Create payment record here.
        I.send_income_notification

    # Steps.

    def find_profile(self, ctx):

        profile = self.load_profile(ctx.profile_id)
        return Success(profile=profile)

    def increase_balance(self, ctx):

        self.add_balance(ctx.profile, ctx.amount)
        return Success()

    def send_income_notification(self, ctx):

        notification = self.send_notification("income", ctx.profile, ctx.amount)
        return Success(notification=notification)

    # Dependencies.

    load_profile: Callable
    add_balance: Callable
    send_notification: Callable


@PutMoneyIntoAccount.put.contract
class Context(BaseModel):

    # Arguments.

    profile_id: ProfileId
    amount: Decimal

    # State.

    profile: Profile
    notification: Notification
