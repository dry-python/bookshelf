from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):

    # FIXME: Use email as username.  The username field should not be
    # used anywhere.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    balance = models.DecimalField(max_digits=10, decimal_places=2)
