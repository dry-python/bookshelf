from attr import attrib, attrs
from stories import Result, Success, argument, story


@attrs
class ListNotifications:
    """List user notifications."""

    impl = attrib()

    @story
    @argument("user")
    def list(self):

        self.find_notifications()
        self.show_notifications()

    def find_notifications(self, ctx):

        notifications = self.impl.load_notifications(ctx.user)
        return Success(notifications=notifications)

    def show_notifications(self, ctx):

        return Result(ctx("notifications"))
