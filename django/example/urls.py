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
    path("sign_up/", views.SignUpView.as_view(), name="sign-up"),
    path("profile/", login_required(views.ProfileView.as_view()), name="profile"),
    path(
        "categories/",
        login_required(views.CategoryListView.as_view()),
        name="category-list",
    ),
    path(
        "categories/<int:id>/",
        views.CategoryDetailView.as_view(),
        name="category-detail",
    ),
    path(
        "shop/", login_required(views.CategoryShopView.as_view()), name="category-shop"
    ),
    path(
        "subscribe/<int:id>/",
        login_required(views.BuySubscriptionView.as_view()),
        name="buy-subscription",
    ),
    path("put_money/", login_required(views.PutMoneyView.as_view()), name="put-money"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
