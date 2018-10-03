import debug_toolbar
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import include, path

from example import views


urlpatterns = [
    path("__debug__/", include(debug_toolbar.urls)),
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view()),
    path("sign_up/", views.SignUp.as_view()),
    path("categories/", login_required(views.CategoryList.as_view())),
]
