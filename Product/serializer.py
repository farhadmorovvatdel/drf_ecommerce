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
    total_item_price=serializers.SerializerMethodField()
    total_price=serializers.SerializerMethodField()
   
    class Meta:
        model=OrderItem
        fields=['id','order','product','quantity','unit_price','total_item_price','total_price']
    def get_total_item_price(self,obj):
        return obj.total_item_price()
    
    def get_total_price(self,obj):
        return obj.order.get_total()
    
        
    
 
class OrderSerializer(serializers.ModelSerializer):
    total_price=serializers.SerializerMethodField()
    class Meta:
        model=Order
        fields=['id','user','is_payment','total_price']
    def get_total_price(self,obj):
        return obj.get_total()
    