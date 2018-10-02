from django.contrib import admin

from example.models import Subscription


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):

    list_display = ["user", "category", "expires"]
