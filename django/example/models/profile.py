from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:

        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):

        return self.user.username
