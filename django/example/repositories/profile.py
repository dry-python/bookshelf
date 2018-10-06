from example.models import Profile


def load_profile(user):

    return Profile.objects.get(user=user)


def create_profile(user):

    return Profile.objects.create(user=user, balance=0)
