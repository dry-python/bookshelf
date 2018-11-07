from attr import attrib, attrs
from stories import Result, Success, argument, story


@attrs
class ListNotifications:
    """List user notifications."""

    impl = attrib()

    @story
    @argument("user")
    def list(I):

        I.find_notifications
        I.show_notifications

    def find_notifications(self, ctx):

        notifications = self.impl.load_notifications(ctx.user)
        return Success(notifications=notifications)

    def show_notifications(self, ctx):

        return Result(ctx("notifications"))
