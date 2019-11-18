from attr import attrib
from attr import attrs
from stories import arguments
from stories import Result
from stories import story
from stories import Success


@attrs
class ListNotifications:
    """List user notifications."""

    @story
    @arguments("user")
    def list(I):

        I.find_notifications
        I.show_notifications

    # Steps.

    def find_notifications(self, ctx):

        notifications = self.load_notifications(ctx.user)
        return Success(notifications=notifications)

    def show_notifications(self, ctx):

        return Result({"notifications": ctx.notifications})

    # Dependencies.

    load_notifications = attrib()
