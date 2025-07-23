from rest_framework.views import APIView
from apps.users.serializers import RegisterSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate


class UserSignupAPIView(APIView):
    serializer_class = RegisterSerializer 

    def post(self, request):
        data = request.data 
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_201_CREATED)


class CookieLoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, username=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            res = Response({"message": "로그인 성공띠"}, status=status.HTTP_200_OK)

            # 쿠키에 토큰 저장
            res.set_cookie(
                key="access", value=access_token,
                httponly=True, samesite='Lax'
            )
            res.set_cookie(
                key="refresh", value=refresh_token,
                httponly=True, samesite='Lax'
            )

            return res

        return Response({"message": "이메일이나 비밀번호가 틀렸지롱?ㅋ."}, status=status.HTTP_401_UNAUTHORIZED)


class CookieLogoutView(APIView):
    def post(self, request):
        # refresh 토큰이 쿠키에 있다면 블랙리스트에 추가
        refresh_token = request.COOKIES.get("refresh")
        if refresh_token:
            try:
                token = RefreshToken(refresh_token)
                token.blacklist()
            except Exception:
                # 만료되었거나 이상한 토큰이면 그냥 패스
                pass

        #  쿠키 삭제
        response = Response({"message": "로그아웃 완료"}, status=status.HTTP_200_OK)
        response.delete_cookie("access")
        response.delete_cookie("refresh")
        return response
    
    
class UserInfoAPIView(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serealizer = UserSerializer(request.user)
        return Response(serealizer.data)


class UserUpdateAPIView(APIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원정보 수정 완료!"}, status=status.HTTP_200_OK)
        
    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
