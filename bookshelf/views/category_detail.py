from django.utils.translation import gettext as _
from django.views.generic import TemplateView

from bookshelf.repositories import load_category
from bookshelf.repositories import load_entries
from bookshelf.repositories import load_subscription


class CategoryDetailView(TemplateView):
    template_name = "category_detail.html"

    @property
    def extra_context(self):
        # TODO: Is it better to keep this business logic in the
        # service layer?

        category = load_category(self.kwargs["id"])

        subscription = load_subscription(category, self.request.profile_id)

        if subscription is None:
            return {
                "category": category,
                "error": _("You should subscribe to this category."),
            }

        if subscription.is_expired:
            return {"category": category, "error": _("Your subscription expires.")}

        entries = load_entries(category)

        return {"category": category, "entries": entries}
