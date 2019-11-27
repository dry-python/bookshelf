from typing import List
from typing import Optional

from attr import attrib
from attr import attrs
from pydantic import BaseModel
from stories import arguments
from stories import Result
from stories import story
from stories import Success

from bookshelf.entities import Category
from bookshelf.entities import CategoryId
from bookshelf.entities import Price
from bookshelf.entities import PriceId


@attrs
class ShopCategoryPrices:
    """Show purchase variants for category."""

    @story
    @arguments("category_id", "error_in")
    def show(I):

        I.find_category
        I.find_prices
        I.make_forms
        I.show_purchase_form

    # Steps.

    def find_category(self, ctx):

        category = self.load_category(ctx.category_id)
        return Success(category=category)

    def find_prices(self, ctx):

        prices = self.load_prices(ctx.category)
        return Success(prices=prices)

    def make_forms(self, ctx):

        forms = self.instantiate_forms(prices=ctx.prices, error_in=ctx.error_in)
        return Success(forms=forms)

    def show_purchase_form(self, ctx):

        return Result(
            {"category": ctx.category, "prices": ctx.prices, "forms": ctx.forms}
        )

    # Dependencies.

    load_category = attrib()
    load_prices = attrib()
    instantiate_forms = attrib()


@ShopCategoryPrices.show.contract
class Context(BaseModel):

    # Arguments.

    category_id: CategoryId
    error_in: Optional[PriceId]

    # State.

    category: Category
    prices: List[Price]
    forms: List
