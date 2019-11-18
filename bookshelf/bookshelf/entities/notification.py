from typing import NewType

from attr import attrib
from attr import attrs

from .profile import Profile

NotificationId = NewType("NotificationId", int)


@attrs
class Notification:

    primary_key = attrib(type=NotificationId)
    profile = attrib(type=Profile)
    message = attrib(type=str)
