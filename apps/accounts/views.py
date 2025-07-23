from rest_framework import generics, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Account
from .serializers import AccountSerializer

#  계좌 목록 조회 + 생성
class AccountListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication] # 누가 요청을 보냈는지 확인하는 방식은 JWT 토큰
    permission_classes = [permissions.IsAuthenticated] # 인증된 유저만 이 api를 쓸수있다
    serializer_class = AccountSerializer # 계좌 데이터를 Account 형식으로 처리

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#  계좌 삭제
class AccountDeleteView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication] # 누가 요청을 보냈는지 확인하는 방식은 JWT 토큰
    permission_classes = [permissions.IsAuthenticated]# 인증된 유저만 이 api를 쓸수있다
    serializer_class = AccountSerializer

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)
