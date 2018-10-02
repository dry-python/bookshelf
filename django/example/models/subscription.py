from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from .category import Category


class Subscription(models.Model):

    user = models.ForeignKey(
        User, related_name="subscriptions", on_delete=models.CASCADE
    )

    category = models.ForeignKey(
        Category, related_name="subscriptions", on_delete=models.CASCADE
    )

    expires = models.DateTimeField()

    class Meta:

        verbose_name = _("subscription")
        verbose_name_plural = _("subscriptions")
