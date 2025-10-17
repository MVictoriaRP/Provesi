from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, cantidad_producto, health

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('productos/<int:producto_id>/cantidad/', cantidad_producto),
    path('health/', health),
]
