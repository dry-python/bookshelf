from decimal import Decimal

from attr import evolve
from django.db.models import F
from mappers import Mapper

from bookshelf import models
from bookshelf.entities import Profile

mapper = Mapper(
    Profile,
    models.Profile,
    {"primary_key": "id", "name": ("user", "username"), "email": ("user", "email")},
)


@mapper.reader
def load_profile(user) -> Profile:
    return models.Profile.objects.filter(user=user)


def create_profile(user) -> Profile:
    return models.Profile.objects.create(user=user, balance=0)


def add_balance(profile: Profile, amount: Decimal) -> Profile:
    models.Profile.objects.filter(pk=profile.primary_key).update(
        balance=F("balance") + amount
    )
    return evolve(profile, balance=profile.balance + amount)


def decrease_balance(profile, amount):
    models.Profile.objects.filter(pk=profile.primary_key).update(
        balance=F("balance") - amount
    )
    return evolve(profile, balance=profile.balance - amount)
