from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/users/", include("apps.users.urls")),# users
    path('api/accounts/', include('apps.accounts.urls')),
    path('api/', include('apps.transactions.urls')), 
]
