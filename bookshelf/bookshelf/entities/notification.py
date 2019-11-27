from typing import NewType

from attr import attrs

from .profile import Profile
from .validated import Validated

NotificationId = NewType("NotificationId", int)


@attrs(auto_attribs=True)
class Notification(Validated):

    primary_key: NotificationId
    profile: Profile
    message: str
