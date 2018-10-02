from dependencies import operation
from dependencies.contrib.django import view

from .utils import TemplateMixin


@view
class CategoryList(TemplateMixin):

    template_name = "category_list.html"

    @operation
    def get(render):
        return render()
