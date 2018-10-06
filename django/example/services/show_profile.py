from attr import attrib, attrs
from stories import Result, Success, argument, story


@attrs
class ShowProfile:
    """Show profile together with user related aggregates."""

    @story
    @argument("user")
    def show(self):

        self.find_profile()
        self.show_profile()

    # Points.

    def find_profile(self):

        profile = self.load_profile(self.ctx.user)
        return Success(profile=profile)

    def show_profile(self):

        return Result(self.ctx("user", "profile"))

    # Dependencies.

    load_profile = attrib()
