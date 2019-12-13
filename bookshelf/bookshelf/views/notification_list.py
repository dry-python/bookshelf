from dependencies import Injector
from dependencies import Package
from dependencies import value
from dependencies.contrib.django import template_view


repositories = Package("bookshelf.repositories")


@template_view
class NotificationListView(Injector):

    template_name = "notification_list.html"

    load_notifications = repositories.load_notifications

    @value
    def extra_context(load_notifications, request):

        return {"notifications": load_notifications(request.profile_id)}
