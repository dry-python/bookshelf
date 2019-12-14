from django.db import models

from .category import Category


# FIXME: Rename to book.


class Entry(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    content = models.FileField(upload_to="entries/%Y/%m/%d/", unique=True)
