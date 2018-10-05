from example.models import Category


def categories_without_subscriptions(user):

    return Category.objects.exclude(subscriptions__profile__user=user)
