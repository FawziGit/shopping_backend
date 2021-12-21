from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    barcode = models.CharField(max_length=14)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name


class Basket(models.Model):
    shopping_date = models.DateTimeField(auto_now=True)
    # description = models.TextField()

    def __str__(self):
        return self.shopping_date
