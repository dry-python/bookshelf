from attr import attrib, attrs
from stories import Result, Success, argument, story


@attrs
class ShowProfile:
    """Show profile together with user related aggregates."""

    impl = attrib()

    @story
    @argument("user")
    def show(I):

        I.find_profile
        I.show_profile

    def find_profile(self, ctx):

        profile = self.impl.load_profile(ctx.user)
        return Success(profile=profile)

    def show_profile(self, ctx):

        return Result(ctx("user", "profile"))
