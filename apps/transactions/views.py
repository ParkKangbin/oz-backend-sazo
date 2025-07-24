from django.shortcuts import get_object_or_404
from rest_framework import generics
from apps.transactions.models import TransactionHistory
from apps.transactions.serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated


# 전체 조회 + 생성
class TransactionCreateView(generics.CreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]


class TransactionListView(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    lookup_url_kwarg = "account_id"

    def get_queryset(self):
        user = self.request.user
        # 요청이 들어오면 장고는 path parameter로 넘겨받은 값을 kwargs에 저장합니다. 
        # self.kwargs["account_id"] 로 접근하여 패스파라미터로 넘어온 account_id에 접근이 가능합니다.
        account_id = self.kwargs[self.lookup_url_kwarg]
        queryset = TransactionHistory.objects.filter(account__user=user, account_id=account_id)

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
    lookup_url_kwarg = "transaction_id"

    def get_queryset(self):
        # 장고의 orm 지연평가에 대해서 공부하기
        queryset = TransactionHistory.objects.prefetch_related("account__user").filter(account__user=self.request.user)
        return queryset
