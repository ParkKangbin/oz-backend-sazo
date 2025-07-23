from django.urls import path
from apps.users.views import (
    UserSignupAPIView,
    CookieLoginView,
    CookieLogoutView,
    UserInfoAPIView,
    UserUpdateAPIView
)

urlpatterns = [
    path("signup/", UserSignupAPIView.as_view(), name="user-signup"),
    path('login/', CookieLoginView.as_view(), name='cookie-login'),
    path("logout/", CookieLogoutView.as_view(), name="cookie-logout"),
    path("userview/", UserInfoAPIView.as_view(), name="user-view"),
    path("userupdate/", UserUpdateAPIView.as_view(), name="user-update"),
]