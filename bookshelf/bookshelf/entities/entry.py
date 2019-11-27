from typing import NewType

from attr import attrib
from attr import attrs

from .category import Category
from .validated import Validated

EntryId = NewType("EntryId", int)


@attrs
class Entry(Validated):

    primary_key = attrib(type=EntryId)
    category = attrib(type=Category)
    content = attrib(type=str)
