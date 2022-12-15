from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from authentication.views import CustomUserCreate, LogoutAndBlacklistRefreshTokenForUserView, ChangePasswordView, UpdateProfileView, ObtainTokenPairView

urlpatterns = [
    path('token/obtain/', ObtainTokenPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/revoke/', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist'),
    path('user/password/<int:pk>/', ChangePasswordView.as_view(), name="change_password"),
    path('user/data/<int:pk>/', UpdateProfileView.as_view(), name="change_data"),
]
