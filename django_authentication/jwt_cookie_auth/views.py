from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenRefreshView

from .serializers import RegisterSerializer, LoginSerializer
from .utils import set_auth_cookies, get_tokens_for_user


# Create your views here.
class RegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        tokens = get_tokens_for_user(user)

        response = Response(
            {"message": "User registered successfully"},
            status=status.HTTP_201_CREATED
        )

        set_auth_cookies(
            response,
            access=str(tokens['access']),
            refresh=str(tokens['refresh'])
        )
        return response

class LoginAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data['user']
            tokens = get_tokens_for_user(user)

            response = Response({"message": "Login successful"})
            set_auth_cookies(
                response,
                access=str(tokens['access']),
                refresh=str(tokens['refresh'])
            )
            return response

class LogoutAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        refresh_token = request.COOKIES.get('refresh')
        token = RefreshToken(refresh_token)
        token.blacklist()

        response = Response({"message": "Logged out"})
        response.delete_cookie('access')
        response.delete_cookie('refresh')
        return response


class CookieTokenRefreshView(TokenRefreshView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        request.data['refresh'] = request.COOKIES.get('refresh')
        response = super().post(request, *args, **kwargs)

        response.set_cookie(
            'access',
            response.data['access'],
            httponly=True,
            secure=True,
            samesite='Lax'
        )
        return response
