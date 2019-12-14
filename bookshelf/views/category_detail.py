from dependencies import Injector
from dependencies import Package
from dependencies import this
from dependencies import value
from dependencies.contrib.django import template_view
from django.utils.translation import gettext as _


repositories = Package("bookshelf.repositories")


@template_view
class CategoryDetailView(Injector):

    template_name = "category_detail.html"

    load_category = repositories.load_category

    load_subscription = repositories.load_subscription

    load_entries = repositories.load_entries

    category_id = this.kwargs["id"]

    profile_id = this.request.profile_id

    @value
    def extra_context(
        load_category, load_subscription, load_entries, category_id, profile_id
    ):

        # TODO: Is it better to keep this business logic in the
        # service layer?

        category = load_category(category_id)

        subscription = load_subscription(category, profile_id)

        if subscription is None:
            return {
                "category": category,
                "error": _("You should subscribe to this category."),
            }

        if subscription.is_expired:
            return {"category": category, "error": _("Your subscription expires.")}

        entries = load_entries(category)

        return {"category": category, "entries": entries}
