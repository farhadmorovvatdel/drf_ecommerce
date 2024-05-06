from django .urls import path
from .views import ProductListAPIView,\
ProductDetailAPIView,\
CatgeoryListAPIView,OrdeItemAPIView,\
    RemoveOrderItemAPIView

urlpatterns=[
    path('',ProductListAPIView.as_view()),
    path('<int:pk>/',ProductDetailAPIView.as_view()),
    path('category/',CatgeoryListAPIView.as_view()),
    path('add-to-cart/<int:pk>/',OrdeItemAPIView.as_view()),
    path('remove-from-cart/<int:pk>/',RemoveOrderItemAPIView.as_view()),
]