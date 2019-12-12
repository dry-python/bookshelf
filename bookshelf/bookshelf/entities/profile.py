from datetime import datetime
from decimal import Decimal
from typing import NewType

from attr import attrs

from .price import Price
from .validated import Validated

ProfileId = NewType("ProfileId", int)


@attrs(auto_attribs=True)
class Profile(Validated):

    primary_key: ProfileId
    first_name: str
    last_name: str
    email: str
    date_joined: datetime
    balance: Decimal

    def can_afford(self, price: Price):
        return self.balance > price.cost
