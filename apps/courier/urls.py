# Django
from django.urls import include, path
from rest_framework.routers import DefaultRouter

# Project
from .views import CourierViewSet


router = DefaultRouter(trailing_slash=False)
router.register('couriers', CourierViewSet, 'courier')

urlpatterns = [
    path('', include(router.urls)),
]
