from example.models import Notification


def load_notifications(user):

    return Notification.objects.filter(profile__user=user).order_by("-pk")


def create_notification(profile, message):

    return Notification.objects.create(profile=profile, message=message)
