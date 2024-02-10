from django.shortcuts import render
from rest_framework.decorators  import api_view
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters import rest_framework as filter
#from rest_framework.filters import ProductFilter
from rest_framework.permissions  import IsAuthenticatedOrReadOnly




# Create your views here.
class CustomerViewset(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer
    pagination_class=PageNumberPagination
    

class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    pagination_class=PageNumberPagination
    filter_backends=(filters.SearchFilter,filter.DjangoFilterBackend,)
    filterset_fields=('name',)
    search_fields=('name',)
    permission_classes=(IsAuthenticatedOrReadOnly,)
    
class SaleViewset(viewsets.ModelViewSet):
    queryset=Sale.objects.select_related('product').all()
    serializer_class=SaleSerializer
    pagination_class=PageNumberPagination
    search_fields=('product__name',)
    permission_classes=(IsAuthenticatedOrReadOnly,)
    
class PaymentViewset(viewsets.ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer
    pagination_class=PageNumberPagination
    search_field=('customer__name')