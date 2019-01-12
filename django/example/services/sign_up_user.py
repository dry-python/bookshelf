from attr import attrib, attrs
from stories import Failure, Success, argument, story


@attrs
class SignUp:
    """Create user and associated profile for it."""

    @story
    @argument("data")
    @argument("request")
    def register_user(I):

        I.compare_passwords
        I.validate_password_strength
        I.persist_user
        I.encrypt_password
        I.persist_profile
        I.login_user
        I.send_welcome_notification

    # Steps.

    def compare_passwords(self, ctx):

        password1 = ctx.data.pop("password1")
        password2 = ctx.data.pop("password2")
        if password1 != password2:
            return Failure()
        return Success(raw_password=password1)

    def validate_password_strength(self, ctx):

        ok, error = self.validate_password(ctx.raw_password)
        if ok:
            return Success()
        else:
            return Failure(error)

    def persist_user(self, ctx):

        user = self.create_user(ctx.data)
        return Success(user=user)

    def encrypt_password(self, ctx):

        self.save_password(**ctx("user", "raw_password"))
        return Success()

    def persist_profile(self, ctx):

        profile = self.create_profile(ctx.user)
        return Success(profile=profile)

    def login_user(self, ctx):

        self.store_user_in_session(ctx.request, ctx.user)
        return Success()

    def send_welcome_notification(self, ctx):

        notification = self.send_notification("welcome", ctx.profile)
        return Success(notification=notification)

    # Dependencies.

    validate_password = attrib()
    create_user = attrib()
    save_password = attrib()
    create_profile = attrib()
    store_user_in_session = attrib()
    send_notification = attrib()
    messages = attrib()
    create_notification = attrib()
