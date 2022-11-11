from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer, ChangePasswordSerializer, UpdateUserSerializer


class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAndBlacklistRefreshTokenForUserView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, format='json'):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            password = serializer.save()
            if password:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request, format='json'):
        serializer = UpdateUserSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.save()
            if data:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
