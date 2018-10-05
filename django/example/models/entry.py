from django.db import models
from django.utils.translation import gettext_lazy as _

from .category import Category


class Entry(models.Model):

    category = models.ForeignKey(
        Category, related_name="entries", on_delete=models.CASCADE
    )

    content = models.FileField(upload_to="entries/%Y/%m/%d/")

    class Meta:

        verbose_name = _("entry")
        verbose_name_plural = _("entries")

    def __str__(self):

        return self.content.name
