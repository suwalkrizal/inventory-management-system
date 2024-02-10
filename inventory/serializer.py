from rest_framework import serializers
from .models import *
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'name',
            'email',
            'phone_number',)
        model=Customer
    # id=serializers.IntegerField()
    # name=serializers.CharField()
    
class ProductSerializer(serializers.ModelSerializer):
    # category_id= serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    # category=serializers.StringRelatedField()

        
    class Meta:
        fields=(
            'id',
            'name',
            'price',
            'description',
            'quantity',)
        model=Product
        
class SaleSerializer(serializers.ModelSerializer):
    # category_id= serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    # category=serializers.StringRelatedField()
    class Meta:
        fields=(
            'product',
            'customer',
            'quantity_sold',
            'sale_date',
        )
        model=Sale
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        fields=(
            'id',
            'payment_status',
            'customer',
            'amount',
            'payment_date',
        )
        model=Payment