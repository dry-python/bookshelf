from typing import NewType

from attr import attrs

from .validated import Validated

CategoryId = NewType("CategoryId", int)


@attrs(auto_attribs=True)
class Category(Validated):

    primary_key: CategoryId
    name: str
