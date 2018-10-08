from dependencies import operation
from dependencies.contrib.django import view

from .utils import TemplateMixin


@view
class NotificationListView(TemplateMixin):

    template_name = "notification_list.html"

    @operation
    def get(render):

        return render()
