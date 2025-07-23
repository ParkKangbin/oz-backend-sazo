from rest_framework import generics
from apps.transactions.models import TransactionHistory
from apps.transactions.serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated

# 전체 조회 + 생성
class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return TransactionHistory.objects.filter(account__user=user)


        # 필터링 처리
        io_type = self.request.query_params.get("io_type")
        min_amount = self.request.query_params.get("min_amount")
        max_amount = self.request.query_params.get("max_amount")

        if io_type:
            queryset = queryset.filter(io_type=io_type)
        if min_amount:
            queryset = queryset.filter(amountgte=min_amount)
        if max_amount:
            queryset = queryset.filter(amountlte=max_amount)

        return queryset

# 수정/삭제/단일조회
class TransactionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return TransactionHistory.objects.filter(account__user=self.request.user)