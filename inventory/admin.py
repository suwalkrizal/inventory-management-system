from django.contrib import admin
from .models import *

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number',)
    search_fields = ('name', 'email', 'phone_number',)
    list_per_page = 10

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'description', 'quantity',)
    search_fields = ('name', 'description',)
    list_per_page = 10

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('customer','amount', 'payment_date','payment_status')
    search_fields = ('customer__name', 'product',)
    list_per_page = 10


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'quantity_sold', 'sale_date',)
    search_fields = ('product__name', 'customer__name',)
    list_per_page = 10
