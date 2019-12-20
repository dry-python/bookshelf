from typing import Callable
from typing import List

from attr import attrs
from pydantic import BaseModel
from stories import arguments
from stories import story
from stories import Success

from bookshelf.entities import Notification


@attrs(auto_attribs=True)
class SendNotifications:
    """Send butch of notifications to user they belong."""

    @story
    @arguments("notifications")
    def send(I):

        I.persist_notifications
        I.broadcast_events

    # Steps.

    def persist_notifications(self, ctx):

        # TODO: Return persisted objects and use them in the next
        # method.
        self.create_notifications(ctx.notifications)
        return Success()

    def broadcast_events(self, ctx):

        # TODO: Send actual message over apns and websocket
        # (https://github.com/centrifugal).
        return Success()

    # Dependencies.

    create_notifications: Callable


@SendNotifications.send.contract
class Context(BaseModel):

    # Arguments.

    notifications: List[Notification]
