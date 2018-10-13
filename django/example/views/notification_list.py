from dependencies import Injector, Package, operation
from dependencies.contrib.django import view


services = Package("example.services")
repositories = Package("example.repositories")
functions = Package("example.functions")


@view
class NotificationListView(Injector):

    template_name = "notification_list.html"

    list_notifications = services.ListNotifications.list

    class impl(Injector):

        load_notifications = repositories.load_notifications

    render = functions.Render

    @operation
    def get(list_notifications, render, user):

        return render(list_notifications(user))
