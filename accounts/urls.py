from django .urls import path
from .views import UserCreateAPIView,UserLoginAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns=[
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',UserCreateAPIView.as_view()),
    path('login/',UserLoginAPIView.as_view())
]