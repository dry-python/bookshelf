from attr import attrib
from attr import attrs
from django.utils.translation import gettext as _


@attrs
class SendNotification:

    messages = attrib()
    create_notification = attrib()

    def do(self, event, profile, *args):

        message = self.messages.build(event, profile, *args)
        notification = self.create_notification(profile, message)
        # TODO: send actual message over websocket.
        return notification


class Messages:
    """All notification messages."""

    def build(self, event, profile, *args):

        return getattr(self, "build_" + event)(profile, *args)

    def build_welcome(self, profile):

        return _("Welcome to our awesome service!")

    def build_subscription(self, profile, category_name):

        return _("You subscribed to %s category") % category_name

    def build_income(self, profile, amount):

        return _("You've payed %d$") % amount
