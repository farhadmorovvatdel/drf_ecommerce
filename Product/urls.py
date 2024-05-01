from django .urls import path
from .views import ProductListAPIView,ProductDetailAPIView,CatgeoryListAPIView

urlpatterns=[
    path('',ProductListAPIView.as_view()),
    path('<int:pk>/',ProductDetailAPIView.as_view()),
    path('category/',CatgeoryListAPIView.as_view())
]