from django.contrib import admin

from example.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = ["profile", "message"]
