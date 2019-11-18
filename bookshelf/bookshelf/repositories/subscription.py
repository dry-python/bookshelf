from datetime import datetime
from typing import Optional

from mappers import Mapper

from bookshelf import models
from bookshelf.entities import Category
from bookshelf.entities import Profile
from bookshelf.entities import Subscription

mapper = Mapper(Subscription, models.Subscription, {"primary_key": "id"})


@mapper.reader
def load_subscription(user: Profile, category: Category) -> Optional[Subscription]:
    return models.Subscription.objects.filter(
        profile__user=user, category=category
    ).order_by("-expires")


def create_subscription(
    profile: Profile, category: Category, expires: datetime
) -> Subscription:
    return models.Subscription.objects.create(
        profile=profile, category=category, expires=expires
    )
