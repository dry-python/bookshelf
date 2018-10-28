from attr import attrib, attrs
from stories import Failure, Success, argument, story


@attrs
class SignUp:
    """Create user and associated profile for it."""

    impl = attrib()

    @story
    @argument("data")
    def register_user(self):

        self.compare_passwords()
        self.validate_password_strength()
        self.persist_user()
        self.encrypt_password()
        self.persist_profile()
        self.login_user()
        self.send_welcome_notification()

    def compare_passwords(self, ctx):

        password1 = ctx.data.pop("password1")
        password2 = ctx.data.pop("password2")
        if password1 != password2:
            return Failure()
        return Success(raw_password=password1)

    def validate_password_strength(self, ctx):

        ok, error = self.impl.validate_password(ctx.raw_password)
        if ok:
            return Success()
        else:
            return Failure(error)

    def persist_user(self, ctx):

        user = self.impl.create_user(ctx.data)
        return Success(user=user)

    def encrypt_password(self, ctx):

        self.impl.save_password(**ctx("user", "raw_password"))
        return Success()

    def persist_profile(self, ctx):

        profile = self.impl.create_profile(ctx.user)
        return Success(profile=profile)

    def login_user(self, ctx):

        self.impl.store_user_in_session(ctx.user)
        return Success()

    def send_welcome_notification(self, ctx):

        notification = self.impl.send_notification("welcome", ctx.profile)
        return Success(notification=notification)
