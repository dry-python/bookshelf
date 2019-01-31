from attr import attrib, attrs
from stories import Result, Success, arguments, story


@attrs
class ShowProfile:
    """Show profile together with user related aggregates."""

    @story
    @arguments("user")
    def show(I):

        I.find_profile
        I.show_profile

    # Steps.

    def find_profile(self, ctx):

        profile = self.load_profile(ctx.user)
        return Success(profile=profile)

    def show_profile(self, ctx):

        return Result({"user": ctx.user, "profile": ctx.profile})

    # Dependencies.

    load_profile = attrib()
