from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Notification(models.Model):

    user = models.ForeignKey(
        User, related_name="notifications", on_delete=models.CASCADE
    )

    message = models.TextField()

    class Meta:

        verbose_name = _("notification")
        verbose_name_plural = _("notifications")
