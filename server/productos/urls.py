from rest_framework import routers
from .api import ProductosViewSet
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

router = routers.DefaultRouter()

router.register('api/productos', ProductosViewSet, 'productos')

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('docs/', include_docs_urls(title='KioskoAPP API')),
    ]
