from dependencies import Injector, Package, operation
from dependencies.contrib.django import view


implemented = Package("example.implemented")
functions = Package("example.functions")


@view
class CategoryListView(Injector):

    template_name = "category_list.html"

    list_categories = implemented.ListCategories.list

    render = functions.Render.do

    @operation
    def get(list_categories, render, user):

        return render(list_categories(user=user))
