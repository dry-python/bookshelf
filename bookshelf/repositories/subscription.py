from datetime import datetime
from typing import Optional

from django.db.models import BooleanField
from django.db.models import Case
from django.db.models import When
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
    is_expired = Case(
        When(expires__lte=now(), then=True), default=False, output_field=BooleanField()
    )
    return models.Subscription.objects.annotate(is_expired=is_expired).filter(
        category_id=category.primary_key, profile_id=profile_id
    )


def create_subscription(
    profile: Profile, category: Category, expires: datetime
) -> Subscription:
    models.Subscription.objects.create(
        profile_id=profile.primary_key,
        category_id=category.primary_key,
        expires=expires,
    )
    # FIXME: Do not fetch the same data twice.
    return load_subscription(category, profile.primary_key)
