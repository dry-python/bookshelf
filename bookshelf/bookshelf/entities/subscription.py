from datetime import datetime
from typing import NewType

from attr import attrib
from attr import attrs

from .category import Category
from .profile import Profile
from .validated import Validated

SubscriptionId = NewType("SubscriptionId", int)


@attrs
class Subscription(Validated):

    primary_key = attrib(type=SubscriptionId)
    profile = attrib(type=Profile)
    category = attrib(type=Category)
    expires = attrib(type=datetime)
