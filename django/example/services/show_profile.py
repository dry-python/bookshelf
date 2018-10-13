from attr import attrib, attrs
from stories import Result, Success, argument, story


@attrs
class ShowProfile:
    """Show profile together with user related aggregates."""

    impl = attrib()

    @story
    @argument("user")
    def show(self):

        self.find_profile()
        self.show_profile()

    def find_profile(self):

        profile = self.impl.load_profile(self.ctx.user)
        return Success(profile=profile)

    def show_profile(self):

        return Result(self.ctx("user", "profile"))
