from django.contrib import admin

from example.models import Entry


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):

    list_display = ["category", "content"]
