from typing import List

from mappers import Mapper

from .profile import config as profile_config
from bookshelf import models
from bookshelf.entities import Notification
from bookshelf.entities import ProfileId

mapper = Mapper(
    Notification,
    models.Notification,
    {"primary_key": "id", "profile": Mapper(profile_config)},
)


@mapper.reader
def load_notifications(profile_id: ProfileId) -> List[Notification]:
    return models.Notification.objects.filter(profile=profile_id).order_by("-pk")


def create_notifications(notifications: List[Notification]) -> None:
    objects = (
        models.Notification(
            profile_id=notification.profile.primary_key, kind=notification.kind.value
        )
        for notification in notifications
    )
    models.Notification.objects.bulk_create(objects)
