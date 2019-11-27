from typing import Callable
from typing import List

from attr import attrs
from pydantic import BaseModel
from stories import arguments
from stories import Result
from stories import story
from stories import Success

from bookshelf.entities import Category
from bookshelf.entities import ProfileId


@attrs(auto_attribs=True)
class ListCategories:
    """List cotegories available to the user."""

    @story
    @arguments("profile_id")
    def list(I):

        I.find_categories
        I.keep_with_subscriptions
        I.show_categories

    # Steps.

    def find_categories(self, ctx):

        categories = self.load_categories()
        return Success(categories=categories)

    def keep_with_subscriptions(self, ctx):

        categories = self.keep_subscriptions(ctx.categories, ctx.profile_id)
        return Success(subscribed=categories)

    def show_categories(self, ctx):

        return Result({"categories": ctx.subscribed})

    # Dependencies.

    load_categories: Callable
    keep_subscriptions: Callable


@ListCategories.list.contract
class Context(BaseModel):

    # Arguments.

    profile_id: ProfileId

    # State.

    categories: List[Category]
    subscribed: List[Category]
