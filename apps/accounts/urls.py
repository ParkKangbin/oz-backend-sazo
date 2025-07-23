from django.urls import path
from .views import AccountListCreateView, AccountDeleteView

urlpatterns = [
    path('', AccountListCreateView.as_view(), name='account-list-create'),
    path('<int:pk>/', AccountDeleteView.as_view(), name='account-delete'),
]
