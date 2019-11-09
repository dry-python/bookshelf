from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Category(models.Model):

    name = models.CharField(max_length=100)

    def get_absolute_url(self):

        return reverse("category-detail", args=(self.pk,))
