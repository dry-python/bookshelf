from decimal import Decimal

from attr import evolve
from django.db.models import F
from mappers import Mapper

from bookshelf import models
from bookshelf.entities import Profile
from bookshelf.entities import ProfileId


mapper = Mapper(
    Profile,
    models.Profile,
    {
        "primary_key": "id",
        "first_name": ("user", "first_name"),
        "last_name": ("user", "last_name"),
        "email": ("user", "email"),
        "date_joined": ("user", "date_joined"),
    },
)


@mapper.reader
def load_profile(profile_id: ProfileId) -> Profile:
    return models.Profile.objects.filter(pk=profile_id)


def create_profile(user) -> Profile:
    return models.Profile.objects.create(user=user, balance=0)


def add_balance(profile: Profile, amount: Decimal) -> Profile:
    # TODO: Use update returning queryset.
    models.Profile.objects.filter(pk=profile.primary_key).update(
        balance=F("balance") + amount
    )
    return evolve(profile, balance=profile.balance + amount)


def decrease_balance(profile, amount):
    # TODO: Use update returning queryset.
    models.Profile.objects.filter(pk=profile.primary_key).update(
        balance=F("balance") - amount
    )
    return evolve(profile, balance=profile.balance - amount)
