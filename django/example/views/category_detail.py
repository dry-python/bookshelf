from dependencies import Injector, Package, operation, this
from dependencies.contrib.django import view
from django.utils.translation import gettext as _


services = Package("example.services")
repositories = Package("example.repositories")
functions = Package("example.functions")


@view
class CategoryDetailView(Injector):

    template_name = "category_detail.html"

    show_category = services.ShowCategory.show

    class impl(Injector):

        load_category = repositories.load_category
        load_subscription = repositories.load_subscription
        load_entries = repositories.load_entries

    render = functions.Render.do

    category_id = this.kwargs["id"]

    @operation
    def get(show_category, category_id, user, render):

        result = show_category.run(category_id, user)
        if result.is_success:
            return render(result.value)
        elif result.failed_on("find_subscription"):
            return render(
                {
                    "category": result.ctx.category,
                    "error": _("You should subscribe to this category."),
                }
            )
        elif result.failed_on("check_expiration"):
            return render(
                {
                    "category": result.ctx.category,
                    "error": _("Your subscription expires."),
                }
            )
