from dependencies import Injector
from dependencies import operation
from dependencies import Package
from dependencies import this
from dependencies.contrib.django import view
from django.utils.translation import gettext as _


implemented = Package("bookshelf.implemented")


@view
class CategoryDetailView(Injector):

    template_name = "category_detail.html"

    show_category = implemented.ShowCategory.show

    category_id = this.kwargs["id"]

    @operation
    def get(show_category, category_id, render, request):

        result = show_category.run(
            category_id=category_id, profile_id=request.profile_id
        )
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
