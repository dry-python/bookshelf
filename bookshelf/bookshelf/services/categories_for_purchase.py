from typing import List

from attr import attrib
from attr import attrs
from pydantic import BaseModel
from stories import arguments
from stories import Result
from stories import story
from stories import Success

from bookshelf.entities import Category
from bookshelf.entities import Price
from bookshelf.entities import ProfileId


@attrs
class CategoriesForPurchase:
    """List categories available to user for purchase."""

    @story
    @arguments("profile_id")
    def list(I):

        I.find_categories
        I.keep_without_subscriptions
        I.keep_with_prices
        I.find_cheapest_prices
        I.show_categories

    # Steps.

    def find_categories(self, ctx):

        categories = self.load_categories()
        return Success(categories=categories)

    def keep_without_subscriptions(self, ctx):

        categories = self.exclude_subscriptions(ctx.categories, ctx.profile_id)
        return Success(no_subscriptions=categories)

    def keep_with_prices(self, ctx):

        categories = self.filter_prices(ctx.no_subscriptions)
        return Success(with_prices=categories)

    def find_cheapest_prices(self, ctx):

        prices = self.load_prices(ctx.with_prices)
        return Success(prices=prices)

    def show_categories(self, ctx):

        return Result({"prices": ctx.prices, "categories": ctx.with_prices})

    # Dependencies.

    load_categories = attrib()
    exclude_subscriptions = attrib()
    filter_prices = attrib()
    load_prices = attrib()


@CategoriesForPurchase.list.contract
class Context(BaseModel):

    # Arguments.

    profile_id: ProfileId

    # State.

    categories: List[Category]
    no_subscriptions: List[Category]
    with_prices: List[Category]
    prices: List[Price]
