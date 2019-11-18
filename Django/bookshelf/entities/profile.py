from decimal import Decimal
from typing import NewType

from attr import attrib
from attr import attrs

ProfileId = NewType("ProfileId", int)


@attrs
class Profile:

    primary_key = attrib(type=ProfileId)
    name = attrib(type=str)
    email = attrib(type=str)
    balance = attrib(type=Decimal)
