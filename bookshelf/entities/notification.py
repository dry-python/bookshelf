from enum import auto
from enum import Enum
from enum import unique
from typing import NewType

from attr import attrs

from .profile import Profile
from .validated import Validated

NotificationId = NewType("NotificationId", int)


@unique
class NotificationKind(Enum):

    welcome = auto()
    income = auto()
    subscription = auto()


@attrs(auto_attribs=True)
class Notification(Validated):

    primary_key: NotificationId
    profile: Profile
    kind: NotificationKind
