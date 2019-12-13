from datetime import datetime
from typing import Optional

from django.db.models import F
from django.utils.timezone import now
from mappers import Evaluated
from mappers import Mapper

from bookshelf import models
from bookshelf.entities import Category
from bookshelf.entities import Profile
from bookshelf.entities import ProfileId
from bookshelf.entities import Subscription


mapper = Mapper(
    Subscription, models.Subscription, {"primary_key": "id", "is_expired": Evaluated()}
)


@mapper.reader
def load_subscription(
    category: Category, profile_id: ProfileId
) -> Optional[Subscription]:
    # FIXME: This comparison does not work.
    return models.Subscription.objects.filter(
        category_id=category.primary_key, profile_id=profile_id
    ).annotate(is_expired=F("expires") <= now())


def create_subscription(
    profile: Profile, category: Category, expires: datetime
) -> Subscription:
    return models.Subscription.objects.create(
        profile=profile, category=category, expires=expires
    )
