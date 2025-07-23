from django.urls import path
from apps.users.views import UserSignupAPIView
from apps.users.views import CookieLoginView
from apps.users.views import CookieLogoutView
from apps.users.views import UserView
urlpatterns = [
    path("signup/", UserSignupAPIView.as_view(), name="user-signup"),
    path('login/', CookieLoginView.as_view(), name='cookie-login'),
    path("logout/", CookieLogoutView.as_view(), name="cookie-logout"),
]