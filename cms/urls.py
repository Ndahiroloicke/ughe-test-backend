from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import HomepageView, LoginView, MeView

urlpatterns = [
    path("homepage/", HomepageView.as_view(), name="homepage"),
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("auth/me/", MeView.as_view(), name="me"),
]
