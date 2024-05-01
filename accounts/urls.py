from django .urls import path
from .views import UserCreateAPIView,UserLoginAPIView
urlpatterns=[
    path('register/',UserCreateAPIView.as_view()),
    path('login/',UserLoginAPIView.as_view())
]