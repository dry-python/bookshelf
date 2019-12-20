from django.db import models

from .profile import Profile


class Notification(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    kind = models.IntegerField()
