from attr import attrib, attrs
from stories import Result, Success, argument, story


@attrs
class ListNotifications:
    """List user notifications."""

    @story
    @argument("user")
    def list(self):

        self.find_notifications()
        self.show_notifications()

    # Points.

    def find_notifications(self):

        notifications = self.load_notifications(self.ctx.user)
        return Success(notifications=notifications)

    def show_notifications(self):

        return Result(self.ctx("notifications"))

    # Dependencies.

    load_notifications = attrib()
