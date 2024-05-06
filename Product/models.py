from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
User=get_user_model()



class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
  
       
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return f"Image of {self.product.name}"
    
class Comment(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='author')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product')
    text=models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.author} - {self.product}'
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
         return f'{self.content_object} - {self.object_id}'

    def unlike(self):
        return  self.delete()

class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type','object_id')
    def __str__(self):
        return f'{self.content_object}- {self.object_id}'
    def RemoveThislike(self):
        return  self.delete()
     
     
     
class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_payment=models.BooleanField(default=False)
    def get_total(self):
        total_amount=0
        for item in self.orderitem_set.prefetch_related('product').all():
            total_amount+=item.total_item_price()
        return total_amount
    
    
    
    def __str__(self):
        return f"Order {self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"
    def total_item_price(self):
        return self.quantity * self.product.price
    
class Discount(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100,unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date=models.DateTimeField()
    end_time=models.DateTimeField()
    is_active=models.BooleanField(default=False)
    def __str__(self):
        return '{self.code} - {self.is_active}'

class OrderDiscount(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    amount_saved = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f'{self.order} - {self.discount}'
    
   
   
       