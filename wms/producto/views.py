from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Producto
from .serializers import ProductoSerializer


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


@api_view(['GET'])
def cantidad_producto(request, producto_id):
    """
    Retorna la cantidad disponible de un producto
    en la bodega principal.
    """
    producto = get_object_or_404(Producto, pk=producto_id)
    return Response({
        "producto_id": producto.id,
        "nombre": producto.nombre,
        "cantidadDisponible": producto.cantidadDisponible
    })


# --- Health check ---
@api_view(['GET'])
def health(request):
    """Health check para monitoreo en AWS."""
    return Response({"status": "ok"})

