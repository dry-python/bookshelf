from example.models import Profile


def create_profile(user):

    return Profile.objects.create(user=user)
