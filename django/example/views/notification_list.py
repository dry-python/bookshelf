from dependencies import Injector, Package, operation
from dependencies.contrib.django import view

from .utils import TemplateMixin


services = Package("example.services")
repositories = Package("example.repositories")


@view
class NotificationListView(TemplateMixin):

    template_name = "notification_list.html"

    list_notifications = services.ListNotifications.list

    class impl(Injector):

        load_notifications = repositories.load_notifications

    @operation
    def get(list_notifications, render, user):

        return render(list_notifications(user))
