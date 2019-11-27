from typing import NewType

from attr import attrib
from attr import attrs

from .validated import Validated

CategoryId = NewType("CategoryId", int)


@attrs
class Category(Validated):

    primary_key = attrib(type=CategoryId)
    name = attrib(type=str)
