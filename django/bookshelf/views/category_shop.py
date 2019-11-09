from dependencies import Injector, Package, operation
from dependencies.contrib.django import view


implemented = Package("bookshelf.implemented")
functions = Package("bookshelf.functions")


@view
class CategoryShopView(Injector):

    template_name = "category_shop.html"

    categories_for_purchase = implemented.CategoriesForPurchase.list

    render = functions.Render.do

    @operation
    def get(categories_for_purchase, user, render):

        return render(categories_for_purchase(user=user))
