from django.db.models import F

from bookshelf.models import Profile


def load_profile(user):

    return Profile.objects.get(user=user)


def create_profile(user):

    return Profile.objects.create(user=user, balance=0)


def save_profile(profile):

    return profile.save()


def add_balance(profile, amount):

    profile.balance = F("balance") + amount


def decrease_balance(profile, amount):

    profile.balance = F("balance") - amount
