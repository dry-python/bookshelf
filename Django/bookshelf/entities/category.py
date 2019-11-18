from typing import NewType

from attr import attrib
from attr import attrs

CategoryId = NewType("CategoryId", int)


@attrs
class Category:

    primary_key = attrib(type=CategoryId)
    name = attrib(type=str)
