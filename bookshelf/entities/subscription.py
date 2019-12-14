from datetime import datetime
from typing import NewType

from attr import attrs

from .category import Category
from .profile import Profile
from .validated import Validated

SubscriptionId = NewType("SubscriptionId", int)


@attrs(auto_attribs=True)
class Subscription(Validated):

    primary_key: SubscriptionId
    profile: Profile
    category: Category
    expires: datetime
    is_expired: bool
