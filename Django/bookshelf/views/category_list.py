from dependencies import Injector
from dependencies import operation
from dependencies import Package
from dependencies.contrib.django import view


implemented = Package("bookshelf.implemented")
functions = Package("bookshelf.functions")


@view
class CategoryListView(Injector):

    template_name = "category_list.html"

    list_categories = implemented.ListCategories.list

    render = functions.Render.do

    @operation
    def get(list_categories, render, user):

        return render(list_categories(user=user))
