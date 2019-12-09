from dependencies import Injector
from dependencies import operation
from dependencies import Package
from dependencies.contrib.django import view


implemented = Package("bookshelf.implemented")


@view
class CategoryShopView(Injector):

    template_name = "category_shop.html"

    categories_for_purchase = implemented.CategoriesForPurchase.list

    @operation
    def get(categories_for_purchase, render, request):

        return render(categories_for_purchase(profile_id=request.profile_id))
