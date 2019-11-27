from django.db import models

from .category import Category
from .profile import Profile


class Subscription(models.Model):

    profile = models.ForeignKey(
        Profile, related_name="subscriptions", on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category, related_name="subscriptions", on_delete=models.CASCADE
    )

    expires = models.DateTimeField()
