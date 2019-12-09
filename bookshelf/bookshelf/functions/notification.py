from __future__ import annotations

from decimal import Decimal
from typing import Callable

from attr import attrs
from django.utils.translation import gettext as _

from bookshelf.entities import Notification
from bookshelf.entities import Profile


@attrs(auto_attribs=True)
class SendNotification:

    # TODO: Should be a substory.  Creation of the notification,
    # websocket and apns messages should be the steps.

    messages: Messages
    create_notification: Callable[[Profile, str], Notification]

    def do(self, event, profile, *args):

        # TODO: Event should be Enum, not a random string.
        message = self.messages.build(event, profile, *args)
        notification = self.create_notification(profile, message)
        # TODO: Send actual message over apns and websocket
        # (https://github.com/centrifugal).
        return notification


class Messages:
    # TODO: This class should not be used to store text in the
    # database.  It will require complex data migration to fix a
    # simple typo.  We should use it in the template filters and
    # serializer fields only.
    """All notification messages."""

    def build(self, event: str, profile: Profile, *args) -> str:

        return getattr(self, "build_" + event)(profile, *args)

    def build_welcome(self, profile: Profile) -> str:

        return _("Welcome to our awesome service!")

    def build_subscription(self, profile: Profile, category_name: str) -> str:

        return _("You subscribed to %s category") % category_name

    def build_income(self, profile: Profile, amount: Decimal) -> str:

        return _("You've payed %d$") % amount
