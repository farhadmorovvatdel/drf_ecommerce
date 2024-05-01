from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializer import ProductSerializer,CategorySerializer
from rest_framework import generics
from .models import Product,Category
from rest_framework.permissions import IsAuthenticated



class ProductListAPIView(generics.ListAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    

class ProductDetailAPIView(generics.GenericAPIView):
    serializer_class=ProductSerializer
    queryset=Product.objects.all() 
    
    

class CatgeoryListAPIView(generics.ListAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.prefetch_related('products').all()
   
  
        
        
   
