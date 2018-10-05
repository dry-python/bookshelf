from attr import attrib, attrs


@attrs
class SendNotification:

    messages = attrib()
    create_notification = attrib()

    def do(self, profile, event):

        message = self.messages.build(profile, event)
        notification = self.create_notification(profile, message)
        # TODO: send actual message over websocket.
        return notification


class Messages:
    """All notification messages."""

    def build(self, profile, event):

        return getattr(self, "build_" + event)(profile)

    def build_welcome(self, profile):

        return "Welcome to our awesome service!"
