from example.models import Subscription


def load_subscription(user, category):

    return Subscription.objects.filter(profile__user=user, category=category).first()
