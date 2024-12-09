# myapp/models.py

from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100, verbose_name="Restaurant Name")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Price")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    def __str__(self):
        return self.name
