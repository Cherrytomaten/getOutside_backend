from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import MultiPartParser, FormParser

from Backend import settings
from .models import CustomUser
from .serializers import CustomUserSerializer, ChangePasswordSerializer, MyTokenObtainPairSerializer, \
    UpdateUserSerializer, UserSerializer, ProfilePictureSerializer

# custom token
from .token import account_activation_token


class ObtainTokenPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


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
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UpdateProfileView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class ChangePasswordView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class UserView(APIView):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        user_instance = request.user
        serializer = UserSerializer(user_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        user_instance = request.user
        user_instance.delete()
        return Response(
            {"res": "User deleted!"},
            status=status.HTTP_200_OK
        )


'''
class ProfilePictureUpload(UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = ProfilePictureSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save(profile_picture=self.request.data())
'''


class ProfilePictureUpload(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return CustomUser.objects.get(uuid=pk)
        except CustomUser.DoesNotExist:
            return None

    def put(self, request, pk, format=None):
        user_instance = self.get_object(pk)
        if not user_instance:
            return Response(
                {"res": "User with pk does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        file = request.data['file']
        data = {
            'profile_picture': request.data
        }
        serializer = UserSerializer(instance=request.user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


'''
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()

        if not instance:
            return Response(
                {"res": "Object with id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
'''
