from example.models import Notification


def create_notification(profile, message):

    Notification.objects.create(profile=profile, message=message)
