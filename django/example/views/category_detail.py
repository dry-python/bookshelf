from dependencies import operation
from dependencies.contrib.django import view

from .utils import TemplateMixin


@view
class CategoryDetailView(TemplateMixin):

    template_name = "category_detail.html"

    @operation
    def get(render):

        return render()
