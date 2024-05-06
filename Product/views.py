from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializer import ProductSerializer,CategorySerializer,OrderItemSerializer,OrderSerializer
from rest_framework import generics
from .models import Product,Category,OrderItem
from rest_framework.permissions import IsAuthenticated
from .models import Order
from rest_framework.views import APIView

class ProductListAPIView(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    

class ProductDetailAPIView(generics.RetrieveAPIView):
    
    serializer_class=ProductSerializer
    queryset=Product.objects.all()
    
    

class CatgeoryListAPIView(generics.ListAPIView):
    serializer_class=CategorySerializer
    queryset=Category.objects.prefetch_related('products').all()
   
class OrdeItemAPIView(generics.CreateAPIView):
    serializer_class = OrderItemSerializer
    queryset = OrderItem.objects.all()
    def post(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            user = request.user
            current_order, created = Order.objects.get_or_create(user=user,is_payment=False)
            current_order_items = current_order.orderitem_set.prefetch_related('product').all()
            current_orderitem = current_order_items.filter(product_id=product.id).first()
            
            if current_orderitem:
                current_orderitem.quantity += 1
                current_orderitem.save()
                serializer = self.serializer_class(current_orderitem)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            ser_data_item = {
                'order': current_order.id,
                'product': product.id,
                'quantity': 1,
                'unit_price': product.price
            }
            serializer = self.serializer_class(data=ser_data_item)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class RemoveOrderItemAPIView(generics.DestroyAPIView):
    serializer_class = OrderItemSerializer
    queryset = Order.objects.all()
    permission_classes=[IsAuthenticated]
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            user = request.user
            current_order = Order.objects.filter(user=user, is_payment=False).first()
            
            if current_order:
                current_order_items = current_order.orderitem_set.prefetch_related('product').all()
                current_orderitem = current_order_items.filter(product_id=product.id).first()
                
                if current_orderitem and current_orderitem.quantity > 1:
                    current_orderitem.quantity -= 1
                    current_orderitem.save()
                    serializer = self.serializer_class(current_orderitem)
                    return Response({'success': 'Product removed from cart'}, status=status.HTTP_200_OK)
                current_order.delete()
                return Response({'success': 'remove item your cart'}, status=status.HTTP_200_OK)
                
            return Response({'error': 'You don\'t have an active cart'}, status=status.HTTP_400_BAD_REQUEST)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
           
            
        
    
    

     
          
       
        
    
      
            
       
        