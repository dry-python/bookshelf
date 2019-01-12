from attr import attrib, attrs
from stories import Result, Success, argument, story


@attrs
class ListNotifications:
    """List user notifications."""

    @story
    @argument("user")
    def list(I):

        I.find_notifications
        I.show_notifications

    # Steps.

    def find_notifications(self, ctx):

        notifications = self.load_notifications(ctx.user)
        return Success(notifications=notifications)

    def show_notifications(self, ctx):

        return Result(ctx("notifications"))

    # Dependencies.

    load_notifications = attrib()
