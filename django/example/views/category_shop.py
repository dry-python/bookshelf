from dependencies import operation
from dependencies.contrib.django import view

from .utils import TemplateMixin


@view
class CategoryShop(TemplateMixin):

    template_name = "category_shop.html"

    @operation
    def get(render):

        return render()
