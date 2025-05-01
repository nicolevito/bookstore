from django.urls import path, include
from rest_framework import routers

from product.viewsets import ProductViewSet 

router = routers.SimpleRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(router.urls)),
]
