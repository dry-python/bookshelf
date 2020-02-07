from django.views.generic import TemplateView

from bookshelf.repositories import load_notifications


class NotificationListView(TemplateView):
    template_name = "notification_list.html"

    @property
    def extra_context(self):
        return {"notifications": load_notifications(self.request.profile_id)}
