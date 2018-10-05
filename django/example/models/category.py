from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):

    name = models.CharField(max_length=100)

    class Meta:

        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):

        return self.name
