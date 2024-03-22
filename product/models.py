from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to='product_images/%Y/%m/%d/', null=True, blank=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"({self.name} - {self.price})"
