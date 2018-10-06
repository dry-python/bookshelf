import debug_toolbar
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.urls import include, path
from django.views.generic import RedirectView

from example import views


urlpatterns = [
    path("", RedirectView.as_view(url="/categories/"), name="home"),
    path("__debug__/", include(debug_toolbar.urls)),
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view(), name="login"),
    path("sign_up/", views.SignUp.as_view(), name="sign-up"),
    path("profile/", login_required(views.Profile.as_view()), name="profile"),
    path(
        "categories/",
        login_required(views.CategoryList.as_view()),
        name="category-list",
    ),
    path("shop/", login_required(views.CategoryShop.as_view()), name="category-shop"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
