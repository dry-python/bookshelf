from django.contrib import admin

from example.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ["name"]
