from rest_framework import serializers
from .models import Product,Category,Order,OrderItem

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['name','price',]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['name']


class OrderItemSerializer(serializers.ModelSerializer):
    # product = ProductSerializer() 
    class Meta:
        model=OrderItem
        fields="__all__"
 
 
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"