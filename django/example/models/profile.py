from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:

        verbose_name = _("profile")
        verbose_name_plural = _("profiles")
