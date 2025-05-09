from django.db import models




class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField(max_length=300)
    description = models.TextField(max_length=10000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField() # Quantity in stock


    def __str__(self):
        return self.name