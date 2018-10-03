from django.db import models
from django.utils.translation import gettext_lazy as _

from .profile import Profile


class Notification(models.Model):

    profile = models.ForeignKey(
        Profile, related_name="notifications", on_delete=models.CASCADE
    )

    message = models.TextField()

    class Meta:

        verbose_name = _("notification")
        verbose_name_plural = _("notifications")
