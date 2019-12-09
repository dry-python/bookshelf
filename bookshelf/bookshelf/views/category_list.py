from dependencies import Injector
from dependencies import operation
from dependencies import Package
from dependencies.contrib.django import view


implemented = Package("bookshelf.implemented")


@view
class CategoryListView(Injector):

    template_name = "category_list.html"

    list_categories = implemented.ListCategories.list

    @operation
    def get(list_categories, render, request):

        return render(list_categories(profile_id=request.profile_id))
