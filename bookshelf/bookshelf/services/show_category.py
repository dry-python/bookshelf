from typing import Callable
from typing import List

from attr import attrs
from pydantic import BaseModel
from stories import arguments
from stories import Failure
from stories import Result
from stories import story
from stories import Success

from bookshelf.entities import Category
from bookshelf.entities import CategoryId
from bookshelf.entities import Entry
from bookshelf.entities import ProfileId
from bookshelf.entities import Subscription


@attrs(auto_attribs=True)
class ShowCategory:
    """Show category entries."""

    @story
    @arguments("category_id", "profile_id")
    def show(I):

        I.find_category
        I.find_subscription
        I.check_expiration
        I.find_entries
        I.show_entries

    # Steps.

    def find_category(self, ctx):

        category = self.load_category(ctx.category_id)
        return Success(category=category)

    def find_subscription(self, ctx):

        subscription = self.load_subscription(ctx.profile_id, ctx.category)
        if subscription:
            return Success(subscription=subscription)
        else:
            return Failure()

    def check_expiration(self, ctx):

        if ctx.subscription.is_expired():
            return Failure()
        else:
            return Success()

    def find_entries(self, ctx):

        entries = self.load_entries(ctx.category)
        return Success(entries=entries)

    def show_entries(self, ctx):

        return Result({"category": ctx.category, "entries": ctx.entries})

    # Dependencies.

    load_category: Callable
    load_subscription: Callable
    load_entries: Callable


@ShowCategory.show.contract
class Context(BaseModel):

    # Arguments.

    category_id: CategoryId
    profile_id: ProfileId

    # State.

    category: Category
    subscription: Subscription
    entities: List[Entry]
