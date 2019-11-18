from datetime import datetime
from decimal import Decimal
from typing import NewType

from attr import attrib
from attr import attrs

from .category import Category

PriceId = NewType("PriceId", int)


@attrs
class Price:

    primary_key = attrib(type=PriceId)
    category = attrib(type=Category)
    from_date = attrib(type=datetime)
    cost = attrib(type=Decimal)
    period = attrib(type=int)
