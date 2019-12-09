from dependencies import Injector
from dependencies import operation
from dependencies import Package
from dependencies.contrib.django import view


implemented = Package("bookshelf.implemented")


@view
class NotificationListView(Injector):

    template_name = "notification_list.html"

    list_notifications = implemented.ListNotifications.list

    @operation
    def get(list_notifications, render, request):

        return render(list_notifications(profile_id=request.profile_id))
