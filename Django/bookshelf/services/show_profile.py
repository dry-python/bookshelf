from attr import attrib
from attr import attrs
from stories import arguments
from stories import Result
from stories import story
from stories import Success


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
