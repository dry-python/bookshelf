from example.models import Category


def categories_with_subscriptions(user):

    return Category.objects.filter(subscriptions__profile__user=user)


def categories_without_subscriptions(user):

    return Category.objects.exclude(subscriptions__profile__user=user)
