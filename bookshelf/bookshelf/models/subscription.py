from django.db import models

from .category import Category
from .profile import Profile


class Subscription(models.Model):

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    expires = models.DateTimeField()

    class Meta:

        unique_together = ['profile', 'category']
