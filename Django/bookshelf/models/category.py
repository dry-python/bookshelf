from django.db import models
from django.urls import reverse


class Category(models.Model):

    name = models.CharField(max_length=100)

    def get_absolute_url(self):

        return reverse("category-detail", args=(self.pk,))
