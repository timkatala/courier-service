# Django
from django.contrib import admin
from django.urls import path, include

# Django Rest Framework
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# External API Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Backend School API",
        default_version='v1',
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)
urlpatterns = [
    path('', include('apps.courier.urls')),
    path('', include('apps.order.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc')
]
