# Django
from django.urls import include, path
from rest_framework.routers import DefaultRouter

# Project
from .views import OrderViewSet


router = DefaultRouter(trailing_slash=False)
router.register('orders', OrderViewSet, 'order')

urlpatterns = [
    path('', include(router.urls)),
]
