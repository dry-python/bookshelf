from decimal import Decimal
from typing import NewType

from attr import attrib
from attr import attrs

from .validated import Validated

ProfileId = NewType("ProfileId", int)


@attrs
class Profile(Validated):

    primary_key = attrib(type=ProfileId)
    name = attrib(type=str)
    email = attrib(type=str)
    balance = attrib(type=Decimal)
