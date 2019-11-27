from typing import List

from attr import attrib
from attr import attrs
from pydantic import BaseModel
from stories import arguments
from stories import Result
from stories import story
from stories import Success

from bookshelf.entities import Notification
from bookshelf.entities import ProfileId


@attrs
class ListNotifications:
    """List user notifications."""

    @story
    @arguments("profile_id")
    def list(I):

        I.find_notifications
        I.show_notifications

    # Steps.

    def find_notifications(self, ctx):

        notifications = self.load_notifications(ctx.profile_id)
        return Success(notifications=notifications)

    def show_notifications(self, ctx):

        return Result({"notifications": ctx.notifications})

    # Dependencies.

    load_notifications = attrib()


@ListNotifications.list.contract
class Context(BaseModel):

    # Arguments.

    profile_id: ProfileId

    # State.

    notifications: List[Notification]
