from django.contrib import admin

from example.models import Price


@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):

    list_display = ["category", "from_date", "amount"]
