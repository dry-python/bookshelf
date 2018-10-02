import debug_toolbar
from django.contrib import admin
from django.urls import include, path

from example import views


urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
    path("admin/", admin.site.urls),
    path("categories/", views.CategoryList.as_view()),
]
