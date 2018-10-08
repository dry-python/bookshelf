from attr import attrib, attrs
from stories import Failure, Success, argument, story


@attrs
class SignUp:
    """Create user and associated profile for it."""

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

    # Points.

    def compare_passwords(self):

        password1 = self.ctx.data.pop("password1")
        password2 = self.ctx.data.pop("password2")
        if password1 != password2:
            return Failure()
        return Success(raw_password=password1)

    def validate_password_strength(self):

        ok, error = self.validate_password(self.ctx.raw_password)
        if ok:
            return Success()
        else:
            return Failure(error)

    def persist_user(self):

        user = self.create_user(self.ctx.data)
        return Success(user=user)

    def encrypt_password(self):

        self.save_password(**self.ctx("user", "raw_password"))
        return Success()

    def persist_profile(self):

        profile = self.create_profile(self.ctx.user)
        return Success(profile=profile)

    def login_user(self):

        self.store_user_in_session(self.ctx.user)
        return Success()

    def send_welcome_notification(self):

        notification = self.send_notification("welcome", self.ctx.profile)
        return Success(notification=notification)

    # Dependencies.

    validate_password = attrib()
    create_user = attrib()
    save_password = attrib()
    create_profile = attrib()
    store_user_in_session = attrib()
    send_notification = attrib()
