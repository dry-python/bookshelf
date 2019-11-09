from django.db import models

from .profile import Profile


class Notification(models.Model):

    profile = models.ForeignKey(
        Profile, related_name="notifications", on_delete=models.CASCADE
    )

    message = models.TextField()
