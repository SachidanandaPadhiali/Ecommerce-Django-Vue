from django.db import models

class Product(models.Model):
    # Field to store the product's name
    name = models.CharField(max_length=255)

    # Detailed description of the product
    description = models.TextField()

    # Price: A decimal field that supports numbers up to 999,999.99
    price = models.DecimalField(max_digits=7, decimal_places=2)

    # Stock: A positive integer representing current stock count
    stock = models.PositiveIntegerField()

    def __str__(self):
        # Returns the product name when the object is printed
        return self.name
