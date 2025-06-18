from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # Automatically generates fields based on the Product model
    class Meta:
        model = Product
        # Include all fields in the serialization
        fields = '__all__'