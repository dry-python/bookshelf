from decimal import Decimal
from typing import Callable

from attr import attrs
from pydantic import BaseModel
from stories import arguments
from stories import story
from stories import Success

from bookshelf.entities import Notification
from bookshelf.entities import NotificationKind
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
        I.prepare_income_notification
        I.send_notifications

    # Steps.

    def find_profile(self, ctx):

        profile = self.load_profile(ctx.profile_id)
        return Success(profile=profile)

    def increase_balance(self, ctx):

        self.add_balance(ctx.profile, ctx.amount)
        return Success()

    def prepare_income_notification(self, ctx):

        notification = Notification(profile=ctx.profile, kind=NotificationKind.income)
        return Success(notifications=[notification])

    # Dependencies.

    load_profile: Callable
    add_balance: Callable
    send_notifications: story


@PutMoneyIntoAccount.put.contract
class Context(BaseModel):

    # Arguments.

    profile_id: ProfileId
    amount: Decimal

    # State.

    profile: Profile
