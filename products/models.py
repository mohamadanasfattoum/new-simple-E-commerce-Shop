from django.db import models

class Stock(models.Model):
    quantity = models.IntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField('Product', related_name='stocks')

    def __str__(self):
        return f"{self.quantity}"


class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField(max_length=300)
    description = models.TextField(max_length=10000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.OneToOneField(Stock, on_delete=models.CASCADE, related_name='product')


    def __str__(self):
        return self.name