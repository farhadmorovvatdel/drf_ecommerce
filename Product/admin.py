from django.contrib import admin
from .models import Product,Category,Order,OrderItem,Discount,OrderDiscount


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Discount)
admin.site.register(OrderDiscount)