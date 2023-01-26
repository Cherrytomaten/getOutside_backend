from django.template.defaulttags import url
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from authentication.views import CustomUserCreate, LogoutAndBlacklistRefreshTokenForUserView, ChangePasswordView, \
    UpdateProfileView, ObtainTokenPairView, UserView, ProfilePictureUpload
from authentication.mailView import ConfirmEmail, ActivateUser, ResetPassword

urlpatterns = [
    path('token/obtain/', ObtainTokenPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/revoke/', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist'),
    path('user/password/<str:pk>/', ChangePasswordView.as_view(), name="change_password"),
    path('user/data/<str:pk>/', UpdateProfileView.as_view(), name="change_data"),
    path('user/', UserView.as_view(), name="get_user"),
    path('user/upload/<int:pk>', ProfilePictureUpload.as_view(), name="uploadProfilePicture"),
    path('user/confirm-email/', ConfirmEmail.as_view(), name="confirmEmail"),
    path('user/activate/', ActivateUser.as_view(), name="activateUser"),
    path('user/password/reset/', ResetPassword.as_view(), name="resetPassword")
]
