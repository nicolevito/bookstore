from django.urls import path, include
from rest_framework import routers

from order import viewset

router = routers.SimpleRouter()
router.register(r'order', viewset.OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls)),
]
