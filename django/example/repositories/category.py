from example.models import Category


def categories():

    return Category.objects.all()


def categories_with_subscriptions(user):

    return Category.objects.filter(subscriptions__profile__user=user)


def exclude_categories_with_subscriptions(categories, user):

    return categories.exclude(subscriptions__profile__user=user)


def filter_categories_with_prices(categories):

    return categories.filter(prices__isnull=False)
