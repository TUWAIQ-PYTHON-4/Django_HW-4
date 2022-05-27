from django.db import models


class Seller(models.Model):
    name = models.CharField(max_length=50, help_text="The name of the seller.")
    phone = models.CharField(max_length=20, help_text="The phone for the seller.")
    email = models.CharField(max_length=50)
    profile = models.TextField(blank=True)
    photo = models.ImageField(upload_to='seller/photos/')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, help_text="The name of the products.")
    description = models.TextField(blank=True)
    price = models.IntegerField()
    seller = models.ForeignKey(Seller, on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to='product/photos/')

    def __str__(self):
        return self.name
