from typing import List

from mappers import Mapper

from bookshelf import models
from bookshelf.entities import Notification
from bookshelf.entities import Profile
from bookshelf.entities import ProfileId

mapper = Mapper(Notification, models.Notification, {"primary_key": "id"})


@mapper.reader
def load_notifications(profile_id: ProfileId) -> List[Notification]:
    return models.Notification.objects.filter(profile=profile_id).order_by("-pk")


@mapper.reader
def create_notification(profile: Profile, message: str) -> Notification:
    # FIXME: Do not fetch the same data twice.
    created = models.Notification.objects.create(
        profile_id=profile.primary_key, message=message
    )
    return models.Notification.objects.filter(pk=created.pk)
