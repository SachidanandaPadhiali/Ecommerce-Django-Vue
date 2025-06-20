from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.conf import settings
from PIL import Image
from django.core.files import File
import os

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_update(self, serializer):
        product = serializer.save()

        if product.image:
            # Paths
            tmp_path = os.path.join(settings.MEDIA_ROOT, product.image.name)
            final_name = f'images/{product.id}.png'
            final_path = os.path.join(settings.MEDIA_ROOT, final_name)

            # Convert to PNG and save
            with Image.open(tmp_path) as img:
                img = img.convert('RGBA')
                img.save(final_path, 'PNG')

            # Delete old file
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

            # Reload image from renamed file
            with open(final_path, 'rb') as f:
                product.image.save(final_name, File(f), save=False)

            product.save()

    def perform_create(self, serializer):
        product = serializer.save()

        if product.image:
            # Paths
            tmp_path = os.path.join(settings.MEDIA_ROOT, product.image.name)
            final_name = f'images/{product.id}.png'
            final_path = os.path.join(settings.MEDIA_ROOT, final_name)

            # Convert to PNG and save
            with Image.open(tmp_path) as img:
                img = img.convert('RGBA')
                img.save(final_path, 'PNG')

            # Delete old file
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

            # Reload image from renamed file
            with open(final_path, 'rb') as f:
                product.image.save(final_name, File(f), save=False)

            product.save()
