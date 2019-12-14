from django.db import models

from .category import Category


class Price(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    cost = models.DecimalField(max_digits=10, decimal_places=2)

    period = models.IntegerField()

    class Meta:

        unique_together = ["category", "period"]
