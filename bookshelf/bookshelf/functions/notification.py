from __future__ import annotations

from decimal import Decimal
from typing import Callable

from attr import attrs
from django.utils.translation import gettext as _

from bookshelf.entities import Notification
from bookshelf.entities import Profile


@attrs(auto_attribs=True)
class SendNotification:

    messages: Messages
    create_notification: Callable[[Profile, str], Notification]

    def do(self, event, profile, *args):

        message = self.messages.build(event, profile, *args)
        notification = self.create_notification(profile, message)
        # TODO: send actual message over websocket.
        return notification


class Messages:
    """All notification messages."""

    def build(self, event: str, profile: Profile, *args) -> str:

        return getattr(self, "build_" + event)(profile, *args)

    def build_welcome(self, profile: Profile) -> str:

        return _("Welcome to our awesome service!")

    def build_subscription(self, profile: Profile, category_name: str) -> str:

        return _("You subscribed to %s category") % category_name

    def build_income(self, profile: Profile, amount: Decimal) -> str:

        return _("You've payed %d$") % amount
