from typing import NewType

from attr import attrs

from .category import Category
from .validated import Validated

EntryId = NewType("EntryId", int)


@attrs(auto_attribs=True)
class Entry(Validated):

    primary_key: EntryId
    category: Category
    content: str
