from django.urls import path,include
from .views import *
from rest_framework import routers

router=routers.SimpleRouter()
router.register(r'customer',CustomerViewset,basename='customer')
router.register(r'product',ProductViewset,basename='product')
router.register(r'sale',SaleViewset,basename='sale')
router.register(r'payment',PaymentViewset,basename='payment')


urlpatterns = router.urls+[
]