from typing import Callable

from attr import attrs
from stories import arguments
from stories import Failure
from stories import story
from stories import Success

from bookshelf.entities import Notification
from bookshelf.entities import NotificationKind


@attrs(auto_attribs=True)
class SignUp:
    """Create user and associated profile for it."""

    @story
    @arguments("data", "request")
    def register_user(I):

        I.compare_passwords
        I.validate_password_strength
        I.persist_user
        I.encrypt_password
        I.persist_profile
        I.login_user
        I.prepare_welcome_notification
        I.send_notifications

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

        self.save_password(user=ctx.user, raw_password=ctx.raw_password)
        return Success()

    def persist_profile(self, ctx):

        profile = self.create_profile(ctx.user)
        return Success(profile=profile)

    def login_user(self, ctx):

        self.store_user_in_session(ctx.request, ctx.user)
        return Success()

    def prepare_welcome_notification(self, ctx):

        notification = Notification(profile=ctx.profile, kind=NotificationKind.welcome)
        return Success(notifications=[notification])

    # Dependencies.

    validate_password: Callable
    create_user: Callable
    save_password: Callable
    create_profile: Callable
    store_user_in_session: Callable
    send_notifications: story


# FIXME: Define context contract.


# FIXME: Define failure protocol.
