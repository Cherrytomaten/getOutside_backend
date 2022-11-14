from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from authentication.views import CustomUserCreate, LogoutAndBlacklistRefreshTokenForUserView

urlpatterns = [
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/revoke/', LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='blacklist'),
]
