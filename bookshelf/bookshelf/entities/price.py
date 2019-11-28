from datetime import datetime
from datetime import timedelta
from decimal import Decimal
from typing import NewType

from attr import attrs

from .category import Category
from .validated import Validated

PriceId = NewType("PriceId", int)


@attrs(auto_attribs=True)
class Price(Validated):

    primary_key: PriceId
    category: Category
    from_date: datetime
    cost: Decimal
    period: int

    def subscription_expiration(self, current_date: datetime) -> datetime:
        return current_date + timedelta(days=self.period)
