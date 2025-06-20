from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    # Query for all Product objects from the database
    queryset = Product.objects.all()
    # Serializer to convert Product objects to/from JSON
    serializer_class = ProductSerializer
    # Only allow authenticated users to modify data;
    # read-only access is open to everyone.
    permission_classes = [IsAuthenticatedOrReadOnly]
    permission_classes = [IsAuthenticated]