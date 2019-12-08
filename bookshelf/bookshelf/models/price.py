from django.db import models

from .category import Category


class Price(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    from_date = models.DateField()

    cost = models.DecimalField(max_digits=10, decimal_places=2)

    period = models.IntegerField()
