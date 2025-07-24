from django.urls import path
from apps.transactions.views import (
    TransactionCreateView,
    TransactionListView,
    TransactionRetrieveUpdateDestroyView
)

urlpatterns = [
    path("transactions/", TransactionCreateView.as_view(), name="transactions-create"),
    path("transactions/<int:pk>/", TransactionRetrieveUpdateDestroyView.as_view(), name="transactions-detail"),
    path("accounts/<int:account_id>/transactions/", TransactionListView.as_view(), name="transactions-list"),
]

# http://localhost:8000/api/accounts/1/transactions/ GET
# http://localhost:8000/api/accounts/2/transactions/ GET
# http://localhost:8000/api/accounts/3/transactions/ GET
# kwargs = {
#    "account_id": 1
# }
