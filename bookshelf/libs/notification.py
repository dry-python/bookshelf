from decimal import Decimal

from django.utils.translation import gettext as _

from bookshelf.entities import Profile


# TODO: Rewrite as single dispatch set of functions.


class Messages:
    """All notification messages."""

    def build(self, event: str, profile: Profile, *args) -> str:

        return getattr(self, "build_" + event)(profile, *args)

    def build_welcome(self, profile: Profile) -> str:

        return _("Welcome to our awesome service!")

    def build_subscription(self, profile: Profile, category_name: str) -> str:

        return _("You subscribed to %s category") % category_name

    def build_income(self, profile: Profile, amount: Decimal) -> str:

        return _("You've payed %d$") % amount
