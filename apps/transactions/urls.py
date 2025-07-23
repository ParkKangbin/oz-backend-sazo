from django.urls import path
from apps.transactions.views import (
    TransactionListCreateView,
    TransactionRetrieveUpdateDestroyView
)

urlpatterns = [
    path("transactions/", TransactionListCreateView.as_view(), name="transactions-list-create"),
    path("transactions/<int:pk>/", TransactionRetrieveUpdateDestroyView.as_view(), name="transactions-detail"),
]