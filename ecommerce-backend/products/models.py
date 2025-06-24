from django.db import models
from uuid import uuid4
from django.core.validators import MinValueValidator, MaxValueValidator

def rename_image_to_id(instance, filename):
    ext = filename.split('.')[-1]
    # Temporarily save with a UUID, then rename after save
    return f'images/tmp/{uuid4()}.{ext}'

class Product(models.Model):
    # Field to store the product's name
    name = models.CharField(max_length=255)

    # Detailed description of the product
    description = models.TextField()

    # Price: A decimal field that supports numbers up to 999,999.99
    price = models.DecimalField(max_digits=7, decimal_places=2)

    # Stock: A positive integer representing current stock count
    stock = models.PositiveIntegerField()

    image = models.ImageField(upload_to=rename_image_to_id, blank=True, null=True)

    rating = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=0.0)

    isOnSale = models.BooleanField(default=False)

    def __str__(self):
        # Returns the product name when the object is printed
        return self.name  