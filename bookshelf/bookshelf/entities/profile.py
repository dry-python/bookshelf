from decimal import Decimal
from typing import NewType

from attr import attrs

from .validated import Validated

ProfileId = NewType("ProfileId", int)


@attrs(auto_attribs=True)
class Profile(Validated):

    primary_key: ProfileId
    name: str
    email: str
    balance: Decimal
