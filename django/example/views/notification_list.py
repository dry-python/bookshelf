from dependencies import Injector, Package, operation
from dependencies.contrib.django import view


implemented = Package("example.implemented")
functions = Package("example.functions")


@view
class NotificationListView(Injector):

    template_name = "notification_list.html"

    list_notifications = implemented.ListNotifications.list

    render = functions.Render.do

    @operation
    def get(list_notifications, user, render):

        return render(list_notifications(user))
