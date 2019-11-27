from typing import Callable

from attr import attrs
from pydantic import BaseModel
from stories import arguments
from stories import Result
from stories import story
from stories import Success

from bookshelf.entities import Profile
from bookshelf.entities import ProfileId


@attrs(auto_attribs=True)
class ShowProfile:
    """Show profile together with user related aggregates."""

    @story
    @arguments("profile_id")
    def show(I):

        I.find_profile
        I.show_profile

    # Steps.

    def find_profile(self, ctx):

        profile = self.load_profile(ctx.profile_id)
        return Success(profile=profile)

    def show_profile(self, ctx):

        return Result({"profile": ctx.profile})

    # Dependencies.

    load_profile: Callable


@ShowProfile.show.contract
class Context(BaseModel):

    # Arguments.

    profile_id: ProfileId

    # State.

    profile: Profile
