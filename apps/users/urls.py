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

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, # 토큰 다시받기 
)
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]