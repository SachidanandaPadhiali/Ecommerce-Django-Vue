from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    # Query for all Product objects from the database
    queryset = Product.objects.all()
    # Serializer to convert Product objects to/from JSON
    serializer_class = ProductSerializer
