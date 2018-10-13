from dependencies import Injector, Package, operation
from dependencies.contrib.django import view


services = Package("example.services")
repositories = Package("example.repositories")
functions = Package("example.functions")


@view
class CategoryListView(Injector):

    template_name = "category_list.html"

    list_categories = services.ListCategories.list

    class impl(Injector):

        load_categories = repositories.load_categories
        keep_subscriptions = repositories.category.keep_subscribed

    render = functions.Render

    @operation
    def get(list_categories, render, user):

        return render(list_categories(user))
